import json
import os
import platform
from enum import Enum
import random
import uuid
from time import sleep
import requests
import string
import datetime

ENV = 0

ROOT_GROUP_ID = 0
CORRELATION_ID = 0
DEVICE_ID = 0
VEHICLE_ID = 0
F2F_EVENT_ID_1ST = 0
F2F_EVENT_ID_2ND = 0
F2F_EVENT_ID_3RD = 0
SERIAL_NUMBER = 0
COLLISION_EVENT_ID_1ST = 0
COLLISION_EVENT_ID_2ND = 0
COLLISION_EVENT_ID_3RD = 0
FYI_EVENT_ID_1ST = 0
FYI_EVENT_ID_2ND = 0
FYI_EVENT_ID_3RD = 0
POSSIBLE_COLLISION_EVENT_ID_1ST = 0
POSSIBLE_COLLISION_EVENT_ID_2ND = 0
COMPANY_ID = 0
DRIVER_ID = 0

platform = platform.system()
if platform == "Windows":
    API_URL = "https://lytx-testautomation-datamanager.int2.drivecaminc.xyz/"
    DC_URL = "https://dc-int.drivecaminc.xyz/"
    FLEET_URL = "https://ft-int.drivecaminc.xyz/"
    FEATURE_TOGGLE_URL = "https://cloud-lytx-featuretoggle-handler-dev.aws.drivecaminc.xyz/"
    ENV = 'int'

else:
    API_URL = os.getenv("ApiUrl")
    DC_URL = os.getenv("DcUrl")
    FLEET_URL = os.getenv("FleetURL")
    FEATURE_TOGGLE_URL = os.getenv("FtUrl")
    ENV = os.getenv('environmentName')

COMPANY_END_POINT: str = API_URL + "companies"
GROUP_OPTION_END_POINT: str = API_URL + "groupOption"
VEHICLE_END_POINT: str = API_URL + "vehicles"
DEVICE_END_POINT: str = API_URL + "devices"
ASSET_ENDPOINT: str = API_URL + "assets"
FLEET_DATA_END_POINT: str = API_URL + "fleet"
USER_END_POINT: str = API_URL + "users"
EVENT_END_POINT: str = API_URL + "events"
PM_SERVICE_END_POINT: str = API_URL + "prev-maint/service"
PM_SERVICE_VEHICLE_END_POINT: str = API_URL + "prev-maint/serviceVehicleInstance"
BULK_CLEAN_UP: str = API_URL + "cleanUpAll/"
FEATURE_TOGGLE_END_POINT: str = FEATURE_TOGGLE_URL + "featureToggles/"
PM_MAINT_END_POINT: str = API_URL + "prev-maint"
GEOFENCE_END_POINT: str = API_URL + "geoFences"


def bulk_cleanup():
    headers = {'Content-Type': 'application/json'}
    bulk_cleanup_endpoint: str = API_URL + "cleanUpAll/" + CORRELATION_ID
    cleanup_response = requests.request("DELETE", bulk_cleanup_endpoint, headers=headers)

    if cleanup_response.status_code == requests.codes.ok:
        print("Bulk cleanup successful")
    else:
        print("Bulk cleanup failed: " + cleanup_response.text)


class AutomationDataManager:
    def __init__(self):
        self.coach_login = None
        self.driver_login = None
        self.pm_login = None
        self.fd_login = None
        self.vrp_login = None
        self.admin_login = None

        self.F2F_EVENT_ID_1ST = 0
        self.F2F_EVENT_ID_2ND = 0
        self.F2F_EVENT_ID_3RD = 0
        self.COLLISION_EVENT_ID_1ST = 0
        self.COLLISION_EVENT_ID_2ND = 0
        self.COLLISION_EVENT_ID_3RD = 0
        self.FYI_EVENT_ID_1ST = 0
        self.FYI_EVENT_ID_2ND = 0
        self.FYI_EVENT_ID_3RD = 0
        self.POSSIBLE_COLLISION_EVENT_ID_1ST = 0
        self.POSSIBLE_COLLISION_EVENT_ID_2ND = 0

        self.DRIVER_ID = 0

        self.geoFenceId = 0
        self.fenceRollupId = 0
        self.correlationId = 0

    def create_test_credentials(self, test_data_list):
        global ROOT_GROUP_ID, CORRELATION_ID, COMPANY_ID
        # Add Company
        headers = {'Content-Type': 'application/json'}
        company_payload = "{}"
        response = requests.request("POST", COMPANY_END_POINT,
                                    headers=headers, data=company_payload)

        if response.status_code == requests.codes.created:
            company_response = json.loads(response.text)
            ROOT_GROUP_ID = company_response["rootGroupId"]
            CORRELATION_ID = company_response["correlationId"]
            COMPANY_ID = company_response["companyId"]
            companyName = company_response["companyName"]
            print("Company created: " + ROOT_GROUP_ID + " with correlationId: " + CORRELATION_ID
                  + "and company Id: " + str(COMPANY_ID) + " and company name : " + companyName)
        else:
            print("Company creation failed: " + response.text)

        for i in test_data_list:
            self.create_data(i)

    def create_data(self, test_data_enum):
        global ROOT_GROUP_ID, CORRELATION_ID, DEVICE_ID, VEHICLE_ID, F2F_EVENT_ID_1ST, F2F_EVENT_ID_2ND, F2F_EVENT_ID_3RD, FYI_EVENT_ID_1ST, FYI_EVENT_ID_2ND, FYI_EVENT_ID_3RD, SERIAL_NUMBER, \
            COLLISION_EVENT_ID_1ST, COLLISION_EVENT_ID_2ND, COLLISION_EVENT_ID_3RD, POSSIBLE_COLLISION_EVENT_ID_1ST, POSSIBLE_COLLISION_EVENT_ID_2ND, PM_SERVICE_ID, PM_SERVICE_VEHICLE_ID
        match test_data_enum:
            case TestDataEnum.ALLOW_AVL_TRUE | TestDataEnum.ALLOW_AVL_FALSE | TestDataEnum.ENABLE_FUEL_MGMT_UI_TRUE | TestDataEnum.ENABLE_FUEL_MGMT_UI_FALSE | \
                 TestDataEnum.SHOW_IDLE_VIOLATION_TRUE | TestDataEnum.SHOW_IDLE_VIOLATION_FALSE | TestDataEnum.ALLOW_SELF_COACH_TRUE | TestDataEnum.ALLOW_SELF_COACH_FALSE | \
                 TestDataEnum.ENABLE_REMOTE_COACH_TRUE | TestDataEnum.ENABLE_REMOTE_COACH_FALSE | TestDataEnum.ENABLE_EVENT_FOLLOW_DRIVER_TRUE | TestDataEnum.ENABLE_EVENT_FOLLOW_DRIVER_FALSE | \
                 TestDataEnum.ENABLE_LVS_TRUE | TestDataEnum.ENABLE_LVS_FALSE | TestDataEnum.ENABLE_DRIVER_ID_TRUE | TestDataEnum.ENABLE_DRIVER_ID_FALSE | \
                 TestDataEnum.ENABLE_FLEET_PM_TRUE | TestDataEnum.ENABLE_FLEET_PM_FALSE | TestDataEnum.ENABLE_FACE_ID_TRUE | TestDataEnum.ENABLE_FACE_ID_FALSE | \
                 TestDataEnum.ENABLE_DVIR_TRUE | TestDataEnum.ENABLE_DVIR_FALSE | TestDataEnum.ENABLE_ASSET_TRACKING_TRUE | TestDataEnum.ENABLE_ASSET_TRACKING_FALSE | \
                 TestDataEnum.ENABLE_LICENSE_MANAGEMENT_TRUE | TestDataEnum.ENABLE_LICENSE_MANAGEMENT_FALSE:
                self.set_group_option(test_data_enum)

            case TestDataEnum.LYTX_DVIR_WEB__ENABLE_INSPECTION_SCHEDULE | TestDataEnum.LYTX_FLEET_WEB__ENABLE_UNIFIED_FLEET_DATA:
                self.enable_feature_toggle(test_data_enum)

            case TestDataEnum.VEHICLE:
                # Add Vehicle
                headers = {'Content-Type': 'application/json'}
                vehicle_payload = {"groupId": ROOT_GROUP_ID, "correlationId": CORRELATION_ID}
                json_vehicle_payload = json.dumps(vehicle_payload)
                response = requests.request("POST", VEHICLE_END_POINT,
                                            headers=headers, data=json_vehicle_payload)

                if response.status_code == requests.codes.created:
                    vehicle_response = json.loads(response.text)
                    VEHICLE_ID = vehicle_response["vehicleId"]
                    print("Vehicle created: " + VEHICLE_ID)
                else:
                    print("Vehicle creation failed: " + response.text)

            case TestDataEnum.DEVICE:
                # Add Device
                headers = {'Content-Type': 'application/json'}
                device_payload = {"correlationId": CORRELATION_ID}
                json_device_payload = json.dumps(device_payload)
                response = requests.request("POST", DEVICE_END_POINT,
                                            headers=headers, data=json_device_payload)

                if response.status_code == requests.codes.created:
                    device_response = json.loads(response.text)
                    DEVICE_ID = device_response["id"]
                    SERIAL_NUMBER = device_response["serialNumber"]
                    print("Device created: " + DEVICE_ID)
                else:
                    print("Device creation failed: " + response.text)

                # Associate Device to Vehicle
                headers = {'Content-Type': 'application/json'}
                association_payload = {"deviceId": DEVICE_ID, "groupId": ROOT_GROUP_ID,
                                       "vehicleId": VEHICLE_ID, "correlationId": CORRELATION_ID}
                json_association_payload = json.dumps(association_payload)
                response = requests.request("POST", DEVICE_END_POINT + "/association", headers=headers,
                                            data=json_association_payload)

                if response.status_code == requests.codes.ok:
                    print("Device " + DEVICE_ID + " successfully associated to Vehicle: " + VEHICLE_ID)
                else:
                    print("Device association failed: " + response.text)

                # Add odometer data to vehicle
                sleep(3)  # sleep here to wait for the device saved to db
                headers = {'Content-Type': 'application/json'}
                association_payload = {"SerialNumber": SERIAL_NUMBER,
                                       "OdometerKm": "9527"}
                json_association_payload = json.dumps(association_payload)
                response = requests.request("POST", PM_MAINT_END_POINT + "/message", headers=headers,
                                            data=json_association_payload)

                if response.status_code == requests.codes.created:
                    print("Set Odometer data to Vehicle: " + VEHICLE_ID + " successfully.")
                else:
                    print("Failed to set Odometer data to Vehicle: " + VEHICLE_ID + " failed: " + response.text)

            case TestDataEnum.ASSET:
                # Add Asset
                headers = {'Content-Type': 'application/json'}
                assetName = str(uuid.uuid1())
                asset_payload = {
                    "GroupId": ROOT_GROUP_ID,
                    "AssetName": "test_" + assetName,
                    "AssetStatusId": 1,
                    "AssetTypeId": 1,
                    "AssetDescription": "test_desc_" + str(random.randint(1, 1000)),
                    "AssetSerial": "test_serial_" + assetName,
                    "CompanyId": COMPANY_ID,
                    "ClientSecret": "dbda12b2-7579-42f4-aac6-e68f4d7aebba"
                }
                json_asset_payload = json.dumps(asset_payload)
                response = requests.request("POST", ASSET_ENDPOINT,
                                            headers=headers, data=json_asset_payload)

                if response.status_code == requests.codes.created:
                    asset_response = json.loads(response.text)
                    ASSET_ID = asset_response["assetId"]
                    print("Asset created: " + ASSET_ID)
                else:
                    print("Asset creation failed: " + response.text)

            case TestDataEnum.DRIVER:
                # Add Driver
                headers = {'Content-Type': 'application/json'}
                user_payload = {
                    "lastName": "Test",
                    "firstName": "Driver",
                    "userRoles": [{
                        "roleId": "4",
                        "groupId": ROOT_GROUP_ID
                    }],
                    "rootGroupId": ROOT_GROUP_ID,
                    "isLoginEnabled": "true",
                    "email": "123@asd.co",
                    "password": "Login123!",
                    "correlationId": CORRELATION_ID
                }
                json_user_payload = json.dumps(user_payload)
                response = requests.request("POST", USER_END_POINT, headers=headers, data=json_user_payload)
                driver_response = json.loads(response.text)
                self.DRIVER_ID = driver_response["userId"]
                self.driver_login = driver_response["userName"]

                if response.status_code == requests.codes.created:
                    print("Driver created: " + self.driver_login)
                else:
                    print("Driver creation failed: " + response.text)

            case TestDataEnum.COACH:
                # Add Coach
                headers = {'Content-Type': 'application/json'}
                coach_payload = {
                    "lastName": "user",
                    "firstName": "coach",
                    "userRoles": [{
                        "roleId": "38",
                        "groupId": ROOT_GROUP_ID
                    }, {
                        "roleId": "5",
                        "groupId": ROOT_GROUP_ID
                    }],
                    "rootGroupId": ROOT_GROUP_ID,
                    "isLoginEnabled": "true",
                    "email": "123@asd.co",
                    "password": "Login123!",
                    "correlationId": CORRELATION_ID
                }
                json_coach_payload = json.dumps(coach_payload)
                response = requests.request("POST", USER_END_POINT, headers=headers,
                                            data=json_coach_payload)
                coach_response = json.loads(response.text)
                self.coach_login = coach_response["userName"]

                if response.status_code == requests.codes.created:
                    print("Coach created: " + self.coach_login)
                else:
                    print("Coach creation failed: " + response.text)

            case TestDataEnum.PROGRAM_MANAGER:
                # Add Program Manager
                headers = {'Content-Type': 'application/json'}
                pm_payload = {
                    "lastName": "manager",
                    "firstName": "program",
                    "userRoles": [{
                        "roleId": "38",
                        "groupId": ROOT_GROUP_ID
                    }, {
                        "roleId": "10",
                        "groupId": ROOT_GROUP_ID
                    }],
                    "rootGroupId": ROOT_GROUP_ID,
                    "isLoginEnabled": "true",
                    "email": "123@asd.co",
                    "password": "Login123!",
                    "correlationId": CORRELATION_ID
                }
                json_pm_payload = json.dumps(pm_payload)
                response = requests.request("POST", USER_END_POINT, headers=headers,
                                            data=json_pm_payload)
                pm_response = json.loads(response.text)
                self.pm_login = pm_response["userName"]

                if response.status_code == requests.codes.created:
                    print("PM User created: " + self.pm_login)
                else:
                    print("PM User creation failed: " + response.text)

            case TestDataEnum.ADMIN:
                # Add Admin User
                headers = {'Content-Type': 'application/json'}
                admin_payload = {
                    "lastName": "Admin",
                    "firstName": "test",
                    "userRoles": [{
                        "roleId": "1",
                        "groupId": ROOT_GROUP_ID
                    }],
                    "rootGroupId": ROOT_GROUP_ID,
                    "isLoginEnabled": "true",
                    "email": "123@asd.co",
                    "password": "Login123!",
                    "userTypeId": "1",
                    "isAvlEnabled": "true",
                    "correlationId": CORRELATION_ID
                }
                json_admin_payload = json.dumps(admin_payload)
                response = requests.request("POST", USER_END_POINT, headers=headers,
                                            data=json_admin_payload)
                admin_response = json.loads(response.text)
                self.admin_login = admin_response["userName"]

                if response.status_code == requests.codes.created:
                    print("Admin User created: " + self.admin_login)
                else:
                    print("Admin User creation failed: " + response.text)

            case TestDataEnum.FLEET_DISPATCHER:
                # Add Fleet Dispatcher
                headers = {'Content-Type': 'application/json'}
                fleet_dispatcher_payload = {
                    "lastName": "dispatcher",
                    "firstName": "fleet",
                    "userRoles": [{
                        "roleId": "24",
                        "groupId": ROOT_GROUP_ID
                    }],
                    "rootGroupId": ROOT_GROUP_ID,
                    "isLoginEnabled": "true",
                    "email": "123@asd.co",
                    "password": "Login123!",
                    "correlationId": CORRELATION_ID
                }
                json_fleet_dispatcher_payload = json.dumps(fleet_dispatcher_payload)
                response = requests.request("POST", USER_END_POINT, headers=headers,
                                            data=json_fleet_dispatcher_payload)
                fleet_dispatcher_response = json.loads(response.text)
                self.fd_login = fleet_dispatcher_response["userName"]

                if response.status_code == requests.codes.created:
                    print("Fleet Dispatcher created: " + self.fd_login)
                else:
                    print("Fleet Dispatcher creation failed: " + response.text)

            case TestDataEnum.VIDEO_REVIEWER_PLUS:
                # Add Video Reviewer Plus
                headers = {'Content-Type': 'application/json'}
                user_payload = {
                    "lastName": "Test",
                    "firstName": "Video Reviewer Plus",
                    "userRoles": [{
                        "roleId": "38",
                        "groupId": ROOT_GROUP_ID
                    }, {
                        "roleId": "35",
                        "groupId": ROOT_GROUP_ID
                    }],
                    "rootGroupId": ROOT_GROUP_ID,
                    "isLoginEnabled": "true",
                    "email": "123@asd.co",
                    "password": "Login123!",
                    "correlationId": CORRELATION_ID
                }
                json_user_payload = json.dumps(user_payload)
                response = requests.request("POST", USER_END_POINT, headers=headers, data=json_user_payload)
                video_reviewer_plus_response = json.loads(response.text)
                self.vrp_login = video_reviewer_plus_response["userName"]

                if response.status_code == requests.codes.created:
                    print("Video Reviewer Plus created: " + self.vrp_login)
                else:
                    print("Video Reviewer Plus creation failed: " + response.text)

            case TestDataEnum.F2F_EVENT_1ST:
                # Create a new event then update to F2F
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                F2F_EVENT_ID_1ST = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + F2F_EVENT_ID_1ST)
                else:
                    print("Event creation failed: " + response.text)

                # Update event to F2F
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "Face-To-Face Coaching",
                                        "TaskStatus": "Face-To-Face Coaching"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + F2F_EVENT_ID_1ST, headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + F2F_EVENT_ID_1ST + " was updated successfully")
                else:
                    print("Event update failed: " + F2F_EVENT_ID_1ST + response.text)

                self.F2F_EVENT_ID_1ST = F2F_EVENT_ID_1ST

            case TestDataEnum.F2F_EVENT_2ND:
                # Create a new event then update to F2F
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                F2F_EVENT_ID_2ND = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + F2F_EVENT_ID_2ND)
                else:
                    print("Event creation failed: " + response.text)

                # Update event to F2F
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "Face-To-Face Coaching",
                                        "TaskStatus": "Face-To-Face Coaching"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + F2F_EVENT_ID_2ND, headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + F2F_EVENT_ID_2ND + " was updated successfully")
                else:
                    print("Event update failed: " + F2F_EVENT_ID_2ND + response.text)

                self.F2F_EVENT_ID_2ND = F2F_EVENT_ID_2ND

            case TestDataEnum.F2F_EVENT_3RD:
                # Create a new event then update to F2F
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                F2F_EVENT_ID_3RD = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + F2F_EVENT_ID_3RD)
                else:
                    print("Event creation failed: " + response.text)

                # Update event to F2F
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "Face-To-Face Coaching",
                                        "TaskStatus": "Face-To-Face Coaching"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + F2F_EVENT_ID_3RD, headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + F2F_EVENT_ID_3RD + " was updated successfully")
                else:
                    print("Event update failed: " + F2F_EVENT_ID_3RD + response.text)

                self.F2F_EVENT_ID_3RD = F2F_EVENT_ID_3RD

            case TestDataEnum.FYI_EVENT_1ST:
                # Create a new event then update to FYI
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                FYI_EVENT_ID_1ST = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + FYI_EVENT_ID_1ST)
                else:
                    print("Event creation failed: " + response.text)

                # Update event to FYI
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "FYI Notify",
                                        "TaskStatus": "FYI Notify"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + FYI_EVENT_ID_1ST, headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + FYI_EVENT_ID_1ST + " was updated successfully")
                else:
                    print("Event update failed: " + FYI_EVENT_ID_1ST + response.text)

                self.FYI_EVENT_ID_1ST = FYI_EVENT_ID_1ST

            case TestDataEnum.FYI_EVENT_2ND:
                # Create a new event then update to FYI
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                FYI_EVENT_ID_2ND = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + FYI_EVENT_ID_2ND)
                else:
                    print("Event creation failed: " + response.text)

                # Update event to FYI
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "FYI Notify",
                                        "TaskStatus": "FYI Notify"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + FYI_EVENT_ID_2ND, headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + FYI_EVENT_ID_2ND + " was updated successfully")
                else:
                    print("Event update failed: " + FYI_EVENT_ID_2ND + response.text)

                self.FYI_EVENT_ID_2ND = FYI_EVENT_ID_2ND

            case TestDataEnum.FYI_EVENT_3RD:
                # Create a new event then update to FYI
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                FYI_EVENT_ID_3RD = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + FYI_EVENT_ID_3RD)
                else:
                    print("Event creation failed: " + response.text)

                # Update event to FYI
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "FYI Notify",
                                        "TaskStatus": "FYI Notify"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + FYI_EVENT_ID_3RD, headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + FYI_EVENT_ID_3RD + " was updated successfully")
                else:
                    print("Event update failed: " + FYI_EVENT_ID_3RD + response.text)

                self.FYI_EVENT_ID_3RD = FYI_EVENT_ID_3RD

            case TestDataEnum.COLLISION_EVENT_1ST:
                # Create a new event
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                COLLISION_EVENT_ID_1ST = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + COLLISION_EVENT_ID_1ST)
                else:
                    print("Event creation failed: " + COLLISION_EVENT_ID_1ST + response.text)

                # Update event to COLLISION
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "Collision",
                                        "TaskStatus": "Face-To-Face Coaching"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + COLLISION_EVENT_ID_1ST,
                                            headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + COLLISION_EVENT_ID_1ST + " was updated to COLLISION")
                else:
                    print("Event update failed: " + COLLISION_EVENT_ID_1ST + response.text)

                self.COLLISION_EVENT_ID_1ST = COLLISION_EVENT_ID_1ST

            case TestDataEnum.COLLISION_EVENT_2ND:
                # Create a new event
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                COLLISION_EVENT_ID_2ND = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + COLLISION_EVENT_ID_2ND)
                else:
                    print("Event creation failed: " + COLLISION_EVENT_ID_2ND + response.text)

                # Update event to COLLISION
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "Collision",
                                        "TaskStatus": "Face-To-Face Coaching"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + COLLISION_EVENT_ID_2ND,
                                            headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + COLLISION_EVENT_ID_2ND + " was updated to COLLISION")
                else:
                    print("Event update failed: " + COLLISION_EVENT_ID_2ND + response.text)

                self.COLLISION_EVENT_ID_2ND = COLLISION_EVENT_ID_2ND

            case TestDataEnum.COLLISION_EVENT_3RD:
                # Create a new event
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                COLLISION_EVENT_ID_3RD = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + COLLISION_EVENT_ID_3RD)
                else:
                    print("Event creation failed: " + COLLISION_EVENT_ID_3RD + response.text)

                # Update event to COLLISION
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "Collision",
                                        "TaskStatus": "Face-To-Face Coaching"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + COLLISION_EVENT_ID_3RD,
                                            headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + COLLISION_EVENT_ID_3RD + " was updated to COLLISION")
                else:
                    print("Event update failed: " + COLLISION_EVENT_ID_3RD + response.text)

                # assign driver to the third collision event
                update_event_driver_payload = {"EventDriverId": self.DRIVER_ID,
                                               "DriverAssignmentTypeId": "1"}
                json_updated_event_driver_payload = json.dumps(update_event_driver_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/driver/" + COLLISION_EVENT_ID_3RD,
                                            headers=headers,
                                            data=json_updated_event_driver_payload)

                if response.status_code == requests.codes.ok:
                    print(
                        "Driver:" + self.DRIVER_ID + " is assigned to Event:" + COLLISION_EVENT_ID_3RD + " successfully")
                else:
                    print(
                        "Driver:" + self.DRIVER_ID + " is not assigned to Event:" + COLLISION_EVENT_ID_3RD + response.text)

                self.COLLISION_EVENT_ID_3RD = COLLISION_EVENT_ID_3RD

            case TestDataEnum.POSSIBLE_COLLISION_EVENT_1ST:
                # Create a new event
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                POSSIBLE_COLLISION_EVENT_ID_1ST = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + POSSIBLE_COLLISION_EVENT_ID_1ST)
                else:
                    print("Event creation failed: " + POSSIBLE_COLLISION_EVENT_ID_1ST + response.text)

                # Update event to POSSIBLE COLLISION
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "Possible Collision",
                                        "TaskStatus": "Face-To-Face Coaching"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + POSSIBLE_COLLISION_EVENT_ID_1ST,
                                            headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + POSSIBLE_COLLISION_EVENT_ID_1ST + " was updated to POSSIBLE COLLISION")
                else:
                    print("Event update failed: " + POSSIBLE_COLLISION_EVENT_ID_1ST + response.text)

                self.POSSIBLE_COLLISION_EVENT_ID_1ST = POSSIBLE_COLLISION_EVENT_ID_1ST

            case TestDataEnum.POSSIBLE_COLLISION_EVENT_2ND:
                # Create a new event
                headers = {'Content-Type': 'application/json'}
                event_payload = {"SerialNumber": SERIAL_NUMBER,
                                 "BehaviorName": "cellphone", "correlationId": CORRELATION_ID}
                json_event_payload = json.dumps(event_payload)
                response = requests.request("POST", EVENT_END_POINT, headers=headers,
                                            data=json_event_payload)
                event_response = json.loads(response.text)
                POSSIBLE_COLLISION_EVENT_ID_2ND = event_response["eventId"]

                if response.status_code == requests.codes.created:
                    print("Event created: " + POSSIBLE_COLLISION_EVENT_ID_2ND)
                else:
                    print("Event creation failed: " + POSSIBLE_COLLISION_EVENT_ID_2ND + response.text)

                # Update event to POSSIBLE COLLISION
                headers = {'Content-Type': 'application/json'}
                update_event_payload = {"EventStatus": "Possible Collision",
                                        "TaskStatus": "Face-To-Face Coaching"}
                json_updated_event_payload = json.dumps(update_event_payload)
                response = requests.request("PUT", EVENT_END_POINT + "/status/" + POSSIBLE_COLLISION_EVENT_ID_2ND,
                                            headers=headers,
                                            data=json_updated_event_payload)

                if response.status_code == requests.codes.ok:
                    print("Event " + POSSIBLE_COLLISION_EVENT_ID_2ND + " was updated to POSSIBLE COLLISION")
                else:
                    print("Event update failed: " + POSSIBLE_COLLISION_EVENT_ID_2ND + response.text)

                self.POSSIBLE_COLLISION_EVENT_ID_2ND = POSSIBLE_COLLISION_EVENT_ID_2ND

            case TestDataEnum.CREATE_GEOFENCE:
                headers = {'Content-Type': 'application/json'}
                geofences_payload = {
                    "DeviceId": DEVICE_ID,
                    "VehicleId": VEHICLE_ID,
                    "GroupId": ROOT_GROUP_ID
                }
                json_geofences_payload = json.dumps(geofences_payload)
                response = requests.request("POST", GEOFENCE_END_POINT, headers=headers, data=json_geofences_payload)

                if response.status_code == requests.codes.created:
                    geofence_response = json.loads(response.text)
                    print("GeoFence created!")
                else:
                    print("Adding GeoFence failed: " + response.text)

            case TestDataEnum.FLEET_TRACKING_DATA:
                headers = {'Content-Type': 'application/json'}
                fleet_payload = {"vehicleId": VEHICLE_ID, "groupId": ROOT_GROUP_ID,
                                 "deviceId": DEVICE_ID, "correlationId": CORRELATION_ID}
                json_fleet_payload = json.dumps(fleet_payload)
                response = requests.request("POST", FLEET_DATA_END_POINT,
                                            headers=headers, data=json_fleet_payload)
                fleet_response = json.loads(response.text)
                self.geoFenceId = fleet_response["geoFenceResponse"][0]["geoFenceId"]
                self.fenceRollupId = fleet_response["geoFenceResponse"][0]["fenceRollupId"]
                self.correlationId = fleet_response["geoFenceResponse"][0]["correlationId"]

                if response.status_code == requests.codes.created:
                    print("Fleet data created")
                else:
                    print("Fleet data creation failed: " + fleet_response.text)

            case TestDataEnum.CREATE_GEOFENCE_ACTIVATION:
                headers = {'Content-Type': 'application/json'}
                geofences_activation_payload = {
                    "DeviceId": DEVICE_ID,
                    "VehicleId": VEHICLE_ID,
                    "GroupId": ROOT_GROUP_ID,
                    "GeoFenceId": self.geoFenceId,
                    "FenceRollupId": self.fenceRollupId,
                    "CorrelationId": self.correlationId,
                }
                json_geofences_activation_payload = json.dumps(geofences_activation_payload)
                response = requests.request("POST", GEOFENCE_END_POINT + "/activation", headers=headers,
                                            data=json_geofences_activation_payload)

                if response.status_code == requests.codes.created:
                    print("GeoFence activation created")
                else:
                    print("Adding GeoFence activation failed: " + response.text)

            case TestDataEnum.PM_SERVICE_DATA:
                headers = {'Content-Type': 'application/json'}
                pm_service_payload = {
                    "GroupId": ROOT_GROUP_ID,
                    "Name": 'Testing' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "CreationDate": "2023-04-05",
                    "DeletionDate": None,
                    "aRevision": 123,
                    "aRevisionDate": "2023-03-20",
                    "aUser": self.driver_login,
                    "aHSUser": CORRELATION_ID,
                    "aMachine": "lytx",
                    "DueSoonDays": 99998,
                    "DueSoonHours": 999999,
                    "DueSoonKm": 1000000,
                    "IntervalDays": 99999,
                    "IntervalHours": 9999999,
                    "IntervalKm": 9999999
                }
                json_pm_service_payload = json.dumps(pm_service_payload)
                pm_service_response = requests.request("POST", PM_SERVICE_END_POINT,
                                                       headers=headers, data=json_pm_service_payload)

                if pm_service_response.status_code == requests.codes.created:
                    json_pm_service_response = json.loads(pm_service_response.text)
                    self.pm_service_id = json_pm_service_response["serviceId"]
                    print("PrevMaint ServiceId created: " + self.pm_service_id)
                else:
                    print("PrevMaint ServiceId creation failed: " + pm_service_response.text)

            case TestDataEnum.PM_SERVICE_VEHICLE_DATA:
                headers = {'Content-Type': 'application/json'}
                pm_service_vehicle_payload = {
                    "ServiceId": self.pm_service_id,
                    "VehicleId": VEHICLE_ID,
                    "DueAtKm": 10000504,
                    "Notes": 'Testing' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=100)),
                    "DueAtDate": "2024-05-30",
                    "DueAtHours": 10001499,
                    "HoursAtCompletion": 0,
                    "UntilDueDays": 99999,
                    "UntilDueHours": 9999999,
                    "UntilDueKm": 9999999,
                    "CreationDate": "2023-05-30",
                    "aRevision": 0,
                    "aRevisionDate": "2023-05-30",
                    "aUser": self.driver_login,
                    "aMachine": "lytx",
                    "aHSUser": CORRELATION_ID
                }
                json_pm_service_vehicle_payload = json.dumps(pm_service_vehicle_payload)
                pm_service_vehicle_response = requests.request("POST", PM_SERVICE_VEHICLE_END_POINT,
                                                               headers=headers, data=json_pm_service_vehicle_payload)

                if pm_service_vehicle_response.status_code == requests.codes.created:
                    json_pm_service_vehicle_response = json.loads(pm_service_vehicle_response.text)
                    self.pm_service_vehicle_id = json_pm_service_vehicle_response["serviceVehicleInstanceId"]
                    print("PrevMaint Service Vehicle Instance created: " + self.pm_service_vehicle_id)
                else:
                    print("PrevMaint Service Vehicle Instance creation failed: " + pm_service_vehicle_response.text)

            case TestDataEnum.MESSAGE_SIMULATOR:
                headers = {'Content-Type': 'application/json'}
                now = datetime.datetime.now()
                later = now + datetime.timedelta(0, 10000)
                messageSimulatorPayload = {
                    "serialNumber": "MV00003342",
                    "startTime": now.strftime('%Y-%m-%d %H:%M:%S'),
                    "endTime": later.strftime('%Y-%m-%d %H:%M:%S'),
                    "kafkaTopic": "LegacyGpsV2",
                    "intervalBetweenTrackPointsInMs": 1000,
                    "companyId": 1129,
                    "stackId": 4,
                    "eventRecorderId": "3500FFFF-6B4A-A1A7-D800-22CA712B0000",
                    "groupId": "5100ffff-60b6-d5cd-8c47-22ca712b0000",
                    "rootGroupId": "2BB2D9B4-C801-E111-81CE-E61F13277AAB",
                    "vehicleId": VEHICLE_ID,
                    "modelNumber": "ER-SF300"
                }
                jsonMessageSimulatorPayload = json.dumps(messageSimulatorPayload)
                response = requests.request("POST", self.messageSimulatorEndpoint, headers=headers,
                                            data=jsonMessageSimulatorPayload)
                if response.status_code == requests.codes.ok:
                    print("Successfully added messages")
                else:
                    print("Adding messages failed: " + response.text)

    def set_group_option(self, option_and_key):
        global ROOT_GROUP_ID
        group_option_key = option_and_key.value
        group_option_name = str(option_and_key)
        group_option_value = ""

        if group_option_key < 2000:
            group_option_key = group_option_key - 1000
            group_option_value = "True"
            group_option_name = group_option_name[13:-5]
        else:
            group_option_key = group_option_key - 2000
            group_option_value = "False"
            group_option_name = group_option_name[13:-6]

        # Enable group option
        headers = {'Content-Type': 'application/json'}
        group_option_payload = {"rootGroupId": ROOT_GROUP_ID,
                                "GroupOptions": {str(group_option_key): group_option_value}}
        json_group_option_payload = json.dumps(group_option_payload)
        group_option_response = requests.request("POST", GROUP_OPTION_END_POINT,
                                                 headers=headers, data=json_group_option_payload)

        if group_option_response.status_code == requests.codes.ok:
            print("Group Option Key " + group_option_name + ":" + str(group_option_key) + " is set to " + str(
                group_option_value))
        else:
            print("Failed to set Group Option Key " + group_option_name + ":" + str(
                group_option_key) + group_option_response.text)

    def enable_feature_toggle(self, feature_toggle):
        global ROOT_GROUP_ID
        category_and_feature = str(feature_toggle).split('__')
        category_name = category_and_feature[0][13:].lower()
        feature_name = category_and_feature[1].lower()

        # Enable Feature Toggle
        headers = {'Content-Type': 'application/json'}
        feature_toggle_payload = {"companyIdList": [ROOT_GROUP_ID],
                                  "isEnabled": 'true',
                                  "optionalParameterPerPod": {}
                                  }
        json_feature_toggle_payload = json.dumps(feature_toggle_payload)
        feature_toggle_response = requests.request("PUT",
                                                   FEATURE_TOGGLE_END_POINT + "categoryName/" + category_name + "/feature/" + feature_name,
                                                   headers=headers, data=json_feature_toggle_payload)

        if feature_toggle_response.status_code == requests.codes.ok:
            print("Feature Toggle: " + category_name + "." + feature_name + " is enabled")
        else:
            print("Failed to set Feature Toggle: " + category_name + "." + feature_name + feature_toggle_response.text)


class TestDataEnum(Enum):
    ALLOW_AVL_TRUE = 1039
    ENABLE_FUEL_MGMT_UI_TRUE = 1042
    SHOW_IDLE_VIOLATION_TRUE = 1082
    ALLOW_SELF_COACH_TRUE = 1107
    ENABLE_REMOTE_COACH_TRUE = 1118
    ENABLE_EVENT_FOLLOW_DRIVER_TRUE = 1138
    ENABLE_LVS_TRUE = 1161
    ENABLE_DRIVER_ID_TRUE = 1193
    ENABLE_FLEET_PM_TRUE = 1238
    ENABLE_FACE_ID_TRUE = 1247
    ENABLE_DVIR_TRUE = 1250
    ENABLE_ASSET_TRACKING_TRUE = 1251
    ENABLE_LICENSE_MANAGEMENT_TRUE = 1264

    ALLOW_AVL_FALSE = 2039
    ENABLE_FUEL_MGMT_UI_FALSE = 2042
    SHOW_IDLE_VIOLATION_FALSE = 2082
    ALLOW_SELF_COACH_FALSE = 2107
    ENABLE_REMOTE_COACH_FALSE = 2118
    ENABLE_EVENT_FOLLOW_DRIVER_FALSE = 2138
    ENABLE_LVS_FALSE = 2161
    ENABLE_DRIVER_ID_FALSE = 2193
    ENABLE_FLEET_PM_FALSE = 2238
    ENABLE_FACE_ID_FALSE = 2247
    ENABLE_DVIR_FALSE = 2250
    ENABLE_ASSET_TRACKING_FALSE = 2251
    ENABLE_LICENSE_MANAGEMENT_FALSE = 2264

    VEHICLE = 3000
    ASSET = 3500

    DEVICE = 4000

    DRIVER = 5000
    COACH = 5100
    PROGRAM_MANAGER = 5200
    ADMIN = 5300
    FLEET_DISPATCHER = 5400
    VIDEO_REVIEWER_PLUS = 5500

    FYI_EVENT_1ST = 6000
    FYI_EVENT_2ND = 6001
    FYI_EVENT_3RD = 6002
    F2F_EVENT_1ST = 6100
    F2F_EVENT_2ND = 6101
    F2F_EVENT_3RD = 6102
    COLLISION_EVENT_1ST = 6200
    COLLISION_EVENT_2ND = 6201
    COLLISION_EVENT_3RD = 6202
    POSSIBLE_COLLISION_EVENT_1ST = 6300
    POSSIBLE_COLLISION_EVENT_2ND = 6301

    FLEET_TRACKING_DATA = 7000
    PM_SERVICE_DATA = 7100
    PM_SERVICE_VEHICLE_DATA = 7101
    CREATE_GEOFENCE = 7200
    CREATE_GEOFENCE_ACTIVATION = 7201

    # feature toggles - the "__" separates category name and feature name
    LYTX_DVIR_WEB__ENABLE_INSPECTION_SCHEDULE = 9000
    LYTX_FLEET_WEB__ENABLE_UNIFIED_FLEET_DATA = 9100
