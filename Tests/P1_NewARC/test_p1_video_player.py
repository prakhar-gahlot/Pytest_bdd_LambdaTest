from datetime import datetime, timedelta
from pytest_bdd import scenarios, given, when, then
from Pages.Arc.event_list_page import EventListPage
from Pages.Arc.event_review_page import EventReviewPage
from Pages.Arc.login_page import LoginPage
from Tests.common import ARC_URL, ENV, AutomationDataManager
from TestingData.Int.event_review_data_int import EventReviewDataInt as ERD_INT
from TestingData.Stg.event_review_data_stg import EventReviewDataStg as ERD_STG
from TestingData.Prod.event_review_data_prod import EventReviewDataProd as ERD_PROD

LOGIN_PAGE = 0
EVENT_LIST_PAGE = 0
EVENT_REVIEW_PAGE = 0
ERD = ''
EVENT_REVIEW_ID = 0
DATA_MGR = ''

scenarios('../../Features/P1_NewARC/p1_video_player.feature')


# LQ-11160
@given('"Reviewer" logs in ARC')
def logs_in_arc(browser):
    global LOGIN_PAGE, EVENT_LIST_PAGE, EVENT_REVIEW_PAGE, ERD, DATA_MGR

    DATA_MGR = AutomationDataManager()
    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)
    EVENT_REVIEW_PAGE = EventReviewPage(browser)

    browser.get(ARC_URL)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD

    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.login().click()
    LOGIN_PAGE.search_company().wait_for_element_displayed()
    LOGIN_PAGE.search_company().type_and_auto_search(ERD.company_name)
    LOGIN_PAGE.first_company().click()
    LOGIN_PAGE.select_company().click()


@when('"Reviewer" filtered out some events in new ARC and the user clicks one event review ID and the user checks the event details above event video')
def filter_in_new_tab():
    global EVENT_REVIEW_ID, EVENT_ID
    EVENT_REVIEW_ID = DATA_MGR.create_new_event()

    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID)
    EVENT_LIST_PAGE.filter_button().click()
    EVENT_ID = EVENT_LIST_PAGE.event_id_1st_only().get_text()
    EVENT_LIST_PAGE.review_id_1st().click()


@then('Review ID is displayed correctly and Trigger is displayed correctly and Record Date is displayed based on local time zone and format is YYYY-MM-DD hh:mm AM/PM')
def verify_review_id_and_trigger_and_record_date():
    EVENT_REVIEW_PAGE.review_id().wait_for_expected_text(str(EVENT_REVIEW_ID))
    record_date = EVENT_REVIEW_PAGE.record_date().get_text()
    am_pm = record_date[-2:]
    record_date_time = datetime.strptime(record_date[:-3], '%m/%d/%Y %I:%M')

    assert EVENT_REVIEW_PAGE.review_id().get_text() == str(EVENT_REVIEW_ID)
    assert EVENT_REVIEW_PAGE.trigger().get_text() == ERD.trigger
    assert (am_pm == 'AM' or am_pm == 'PM') is True
    assert record_date_time < datetime.now()
    assert record_date_time > datetime.now() + timedelta(days=-1)

@then('Vehicle ID is displayed as vehicle name and Vehicle type is displayed correctly and Seatbelt is displayed correctly and Audio is displayed correctly and FPS is displayed correctly')
def verify_vehicle_info_audio_fps():
    assert EVENT_REVIEW_PAGE.vehicle_id().get_text() == ERD.vehicle
    assert EVENT_REVIEW_PAGE.vehicle_type().get_text() == ERD.vehicle_type
    assert EVENT_REVIEW_PAGE.seatbelt().get_text() == ERD.seatbelt
    assert EVENT_REVIEW_PAGE.audio().get_text() == ERD.audio
    assert EVENT_REVIEW_PAGE.FPS().get_text() == ERD.fps
