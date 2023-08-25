from datetime import datetime
from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then
from Pages.Arc.event_list_page import EventListPage
from Pages.Arc.login_page import LoginPage
from Tests.common import ARC_URL, ENV, AutomationDataManager
from TestingData.Int.event_review_data_int import EventReviewDataInt as ERD_INT
from TestingData.Stg.event_review_data_stg import EventReviewDataStg as ERD_STG
from TestingData.Prod.event_review_data_prod import EventReviewDataProd as ERD_PROD


LOGIN_PAGE = 0
EVENT_LIST_PAGE = 0
EVENT_REVIEW_PAGE = 0
OUTCOME_TRIGGER_TAB = 0
BEHAVIORS_TAB = 0
COMMENTS_TAB = 0
WS_LOGIN_PAGE = 0
WS_TASK_PAGE = 0
ERD = ''
EVENT_REVIEW_ID = 0
EVENT_ID = ''
DATA_MGR = ''

scenarios('../../Features/P1_NewARC/p1_search_and_event_review.feature')


# LQ-10595
@given('the user logins to ARC')
def login_arc(browser):
    global DATA_MGR, LOGIN_PAGE, EVENT_LIST_PAGE, ERD

    DATA_MGR = AutomationDataManager()
    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD

    browser.get(ARC_URL)

    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.login().click()

    LOGIN_PAGE.search_company().wait_for_element_displayed()
    LOGIN_PAGE.search_company().type_and_auto_search(ERD.company_name)
    LOGIN_PAGE.first_company().click()
    LOGIN_PAGE.select_company().click()


@when('the user input a valid New event Review ID and the user clicks "Filter" button')
def filter_in_new_tab():
    global EVENT_REVIEW_ID, EVENT_ID
    EVENT_REVIEW_ID = DATA_MGR.create_new_event()

    EVENT_LIST_PAGE.new_tab().click()
    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID)
    EVENT_LIST_PAGE.filter_button().click()

@then('the related event is filtered out under the New tab and the event count of New tab is shown')
def verify_new_events_filtered():
    EVENT_LIST_PAGE.search_range_and_results().wait_for_expected_text('1 result')
    creation_date = datetime.strptime(EVENT_LIST_PAGE.creation_date_1st().get_text(), '%Y-%m-%d %I:%M %p')

    assert_that(EVENT_LIST_PAGE.search_range_and_results().get_text(), contains_string(str(EVENT_REVIEW_ID)))
    assert_that(EVENT_LIST_PAGE.search_range_and_results().get_text(), contains_string('1 result'))
    assert_that(EVENT_LIST_PAGE.new_tab().get_text(), contains_string('New (1)'))
    assert EVENT_LIST_PAGE.review_id_1st().get_text() == str(EVENT_REVIEW_ID)
    assert creation_date < datetime.now()
    assert EVENT_LIST_PAGE.vehicle_name_1st().get_text() == ERD.vehicle
    assert EVENT_LIST_PAGE.serial_num_1st().get_text() == ERD.ER

@then('the event list shows columns: "REVIEW ID","EVENT ID","CREATION DATE","VEHICLE NAME","ER SERIAL"')
def verify_event_columns():
    assert EVENT_LIST_PAGE.review_id_title().get_text() == 'REVIEW ID'
    assert EVENT_LIST_PAGE.event_id_title().get_text() == 'EVENT ID'
    assert EVENT_LIST_PAGE.creation_date_title().get_text() == 'CREATION DATE'
    assert EVENT_LIST_PAGE.vehicle_name_title().get_text() == 'VEHICLE NAME'
    assert EVENT_LIST_PAGE.serial_num_title().get_text() == 'ER SERIAL #'
