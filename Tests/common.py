import json
import os
import platform
from time import sleep
import requests
from TestingData.Int.event_review_data_int import EventReviewDataInt as ERD_INT
from TestingData.Stg.event_review_data_stg import EventReviewDataStg as ERD_STG
from TestingData.Prod.event_review_data_prod import EventReviewDataProd as ERD_PROD

ENV = ''
DC_URL = ''
ARC_URL = ''
API_URL = ''
ERD = ''

platform = platform.system()
if platform == "Windows":
    API_URL = "https://lytx-testautomation-datamanager.int2.drivecaminc.xyz/"
    DC_URL = "https://dc-int.drivecaminc.xyz/"
    ARC_URL = "https://lytx-reviewcenter-ui-dev.aws.drivecaminc.xyz/"
    ENV = 'int'
    ERD = ERD_INT

else:
    API_URL = os.getenv("ApiUrl")
    DC_URL = os.getenv("DcUrl")
    ARC_URL = os.getenv("ArcURL")
    ENV = os.getenv('environmentName')

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD

ARC_CREATE_END_POINT: str = API_URL + "arc/create"
EVENT_END_POINT: str = API_URL + "events"


class AutomationDataManager:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}

    def create_new_event(self, video='cellphone', trigger='', behaviors=[]):
        # event video is chosen by behavior name
        new_event_payload = {"SerialNumber": ERD.ER,
                             "BehaviorName": video}
        json_new_event_payload = json.dumps(new_event_payload)
        new_event_response = requests.request("POST", EVENT_END_POINT, headers=self.headers,
                                              data=json_new_event_payload)

        new_event_info = json.loads(new_event_response.text)
        event_cust_id = new_event_info["eventCustId"]

        if new_event_response.status_code == requests.codes.created:
            print("Event created: " + event_cust_id)
        else:
            print("Event creation failed: " + new_event_response.text)

        # update event driver
        sleep(2)
        update_event_driver_payload = {"EventDriverId": ERD.driver_id,
                                       "DriverAssignmentTypeId": "1"}
        json_update_event_driver_payload = json.dumps(update_event_driver_payload)
        update_event_driver_response = requests.request("PUT", EVENT_END_POINT + "/driver/" + event_cust_id,
                                                        headers=self.headers, data=json_update_event_driver_payload)

        if update_event_driver_response.status_code == requests.codes.ok:
            print("Driver:" + ERD.driver_id + " is assigned to Event:" + event_cust_id + " successfully")
        else:
            print("Driver:" + ERD.driver_id + " is not assigned. Message:" + update_event_driver_response.text)

        # push to cloud
        sleep(2)
        arc_create_payload = {"EventCustID": event_cust_id,
                              "actorId": ERD.actor_id}
        json_arc_create_payload = json.dumps(arc_create_payload)
        arc_create_response = requests.request("POST", ARC_CREATE_END_POINT, headers=self.headers,
                                               data=json_arc_create_payload)
        event_info = json.loads(arc_create_response.text)

        unique_event_id = event_info["uniqueEventId"]

        if arc_create_response.status_code == requests.codes.created:
            print("Event is ready for review: " + str(unique_event_id))
        else:
            print("Event push failed: " + arc_create_response.text)

        return unique_event_id
