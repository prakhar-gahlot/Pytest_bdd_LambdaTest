from datetime import datetime
from time import sleep
from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then
from selenium.common.exceptions import TimeoutException
from Pages.Arc.event_list_page import EventListPage
from Pages.Arc.event_review_page import EventReviewPage
from Pages.Arc.outcome_trigger_tab import OutcomeTriggerTab
from Pages.Arc.behaviors_tab import BehaviorsTab
from Pages.Arc.comments_tab import CommentsTab
from Pages.Arc.login_page import LoginPage
from Pages.WS.ws_login_page import WSLoginPage
from Pages.WS.ws_task_page import WSTaskPage
from Tests.common import ARC_URL, DC_URL, ENV, AutomationDataManager
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
EVENT_ID = 0
DATA_MGR = ''

scenarios('../../Features/Smoke/arc_smoke.feature')


# LQ-9709
@given('the user is in the Login page of New ARC and a user has Reviewer role in some companies')
def open_login_page(browser):
    global DATA_MGR, LOGIN_PAGE, EVENT_LIST_PAGE, EVENT_REVIEW_PAGE, OUTCOME_TRIGGER_TAB, BEHAVIORS_TAB, COMMENTS_TAB, \
        WS_LOGIN_PAGE, WS_TASK_PAGE, ERD

    DATA_MGR = AutomationDataManager()
    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)
    EVENT_REVIEW_PAGE = EventReviewPage(browser)
    OUTCOME_TRIGGER_TAB = OutcomeTriggerTab(browser)
    BEHAVIORS_TAB = BehaviorsTab(browser)
    COMMENTS_TAB = CommentsTab(browser)
    WS_LOGIN_PAGE = WSLoginPage(browser)
    WS_TASK_PAGE = WSTaskPage(browser)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD

    browser.get(ARC_URL)

@when('the user inputs valid username and password and the user clicks the Sign in button')
def reviewer_sign_in():
    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)

    LOGIN_PAGE.login().click()

@when('the user select Reviewer role in the Role dropdown list and the user select one company in the company dropdown list and the user clicks the Select button')
def reviewer_select_role_and_company():
    LOGIN_PAGE.search_company().wait_for_element_displayed()
    LOGIN_PAGE.select_role().click()
    LOGIN_PAGE.select_reviewer_role().click()
    LOGIN_PAGE.search_company().type_and_auto_search(ERD.company_name_switch)
    LOGIN_PAGE.first_company().click()
    LOGIN_PAGE.select_company().click()

@then('the Review page is opened')
def verify_event_list_page_opened():
    assert EVENT_LIST_PAGE.title().get_text() == 'Lytx ReviewCenter'

# LQ-10592
@when('the user logins in ARC with Company A')
def go_to_login_page_and_sign_in(browser):
    browser.get(ARC_URL)

    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.login().click()

    LOGIN_PAGE.search_company().wait_for_element_displayed()
    LOGIN_PAGE.select_role().click()
    LOGIN_PAGE.select_reviewer_role().click()
    LOGIN_PAGE.search_company().type_and_auto_search(ERD.company_name_switch)
    LOGIN_PAGE.first_company().click()
    LOGIN_PAGE.select_company().click()

@then('"Reviewing for: Company A" text is displayed behind "Lytx ReviewerCenter" '
      'and "Switch Companies" button with clickable status is displayed behind "Reviewing for: Company A" '
      'and there is a Give Feedback link on the top-right corner')
def verify_selected_company():
    EVENT_LIST_PAGE.company_name().wait_for_expected_text(ERD.company_name_switch)

    assert EVENT_LIST_PAGE.title().get_text() == 'Lytx ReviewCenter'
    assert EVENT_LIST_PAGE.company_name().get_text() == ERD.company_name_switch
    assert EVENT_LIST_PAGE.switch_company().get_text() == 'Switch Companies'
    assert EVENT_LIST_PAGE.give_feedback().get_text() == 'Give Feedback'

# LQ-10693
@when('the user clicks "Switch Companies" button and the user selects one Company from dropdown list and clicks "Select" button')
def go_to_login_page_and_sign_in():
    EVENT_LIST_PAGE.switch_company().click()
    EVENT_LIST_PAGE.search_company_switch_company().wait_for_element_displayed()
    EVENT_LIST_PAGE.search_company_switch_company().type_and_auto_search(ERD.company_name)
    EVENT_LIST_PAGE.first_company().click()
    EVENT_LIST_PAGE.select_company().click()

@then('the Company is switched successfully')
def verify_selected_company():
    EVENT_LIST_PAGE.company_name().wait_for_expected_text(ERD.company_name)

    assert EVENT_LIST_PAGE.title().get_text() == 'Lytx ReviewCenter'
    assert EVENT_LIST_PAGE.company_name().get_text() == ERD.company_name
    assert EVENT_LIST_PAGE.switch_company().get_text() == 'Switch Companies'

# LQ-10596
@when('the user input a range of Review IDs and Clicks "Filter" button')
def filter_in_new_tab():
    review_id_range = ERD.review_id_range_from + '-' + ERD.review_id_range_to

    EVENT_LIST_PAGE.review_id_filter().type(review_id_range)
    EVENT_LIST_PAGE.filter_button().click()

@then('the filtered Result is displayed under new event list correctly by CreationDate ASC and searched new events are displayed on one page without pagination')
def verify_new_events_filtered():
    EVENT_LIST_PAGE.search_range_and_results().wait_for_expected_text('-')
    new_tab_text = EVENT_LIST_PAGE.new_tab().get_text()
    event_count = int(new_tab_text.split('(')[1].split(')')[0])
    creation_date = datetime.strptime(EVENT_LIST_PAGE.creation_date_1st().get_text(), '%Y-%m-%d %I:%M %p')

    assert EVENT_LIST_PAGE.get_row_count() == event_count
    assert EVENT_LIST_PAGE.review_id_1st().get_text() >= ERD.review_id_range_from
    assert EVENT_LIST_PAGE.review_id_1st().get_text() <= ERD.review_id_range_to
    assert creation_date < datetime.now()

@then('the value in each column for the new events are displayed correctly')
def verify_new_tab_event_columns():
    assert EVENT_LIST_PAGE.review_id_title().get_text() == 'REVIEW ID'
    assert EVENT_LIST_PAGE.event_id_title().get_text() == 'EVENT ID'
    assert EVENT_LIST_PAGE.creation_date_title().get_text() == 'CREATION DATE'
    assert EVENT_LIST_PAGE.vehicle_name_title().get_text() == 'VEHICLE NAME'
    assert EVENT_LIST_PAGE.serial_num_title().get_text() == 'ER SERIAL #'
    assert len(EVENT_LIST_PAGE.event_id_1st().get_text()) > 0
    assert len(EVENT_LIST_PAGE.vehicle_name_1st().get_text()) > 0
    assert len(EVENT_LIST_PAGE.serial_num_1st().get_text()) > 0

@when('the user input a range of Review IDs in the filter under the Returned tab and the user Clicks "Filter" button')
def filter_in_returned_tab():
    review_id_range = ERD.review_id_range_from + '-' + ERD.review_id_range_to

    EVENT_LIST_PAGE.return_tab().click()
    EVENT_LIST_PAGE.review_id_filter().type(review_id_range)
    EVENT_LIST_PAGE.filter_button().click()

@then('the filtered Result is displayed under returned event list correctly by CreationDate ASC and searched returned events are displayed on one page without pagination')
def verify_returned_events_filtered():
    EVENT_LIST_PAGE.search_range_and_results().wait_for_expected_text('-')
    returned_tab_text = EVENT_LIST_PAGE.return_tab().get_text()
    event_count = int(returned_tab_text.split('(')[1].split(')')[0])
    creation_date = datetime.strptime(EVENT_LIST_PAGE.creation_date_1st().get_text(), '%Y-%m-%d %I:%M %p')

    assert EVENT_LIST_PAGE.get_row_count() == event_count
    assert EVENT_LIST_PAGE.review_id_1st().get_text() >= ERD.review_id_range_from
    assert EVENT_LIST_PAGE.review_id_1st().get_text() <= ERD.review_id_range_to
    assert creation_date < datetime.now()

@then('the value in each column for the returned events are displayed correctly')
def verify_returned_tab_event_columns():
    assert EVENT_LIST_PAGE.review_id_title().get_text() == 'REVIEW ID'
    assert EVENT_LIST_PAGE.event_id_title().get_text() == 'EVENT ID'
    assert EVENT_LIST_PAGE.creation_date_title().get_text() == 'CREATION DATE'
    assert EVENT_LIST_PAGE.vehicle_name_title().get_text() == 'VEHICLE NAME'
    assert EVENT_LIST_PAGE.serial_num_title().get_text() == 'ER SERIAL #'
    assert len(EVENT_LIST_PAGE.event_id_1st().get_text()) > 0
    assert len(EVENT_LIST_PAGE.vehicle_name_1st().get_text()) > 0
    assert len(EVENT_LIST_PAGE.serial_num_1st().get_text()) > 0

# LQ-11162
@when('the user clicks one reviewID')
def click_first_review_id_new_tab():
    global EVENT_REVIEW_ID, EVENT_ID
    EVENT_REVIEW_ID = DATA_MGR.create_new_event()

    EVENT_LIST_PAGE.new_tab().click()
    EVENT_LIST_PAGE.review_id_filter().clear()
    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID)
    EVENT_LIST_PAGE.filter_button().click()
    EVENT_ID = EVENT_LIST_PAGE.event_id_1st_only().get_text()
    EVENT_LIST_PAGE.review_id_1st().click()

@then('the event review page is opened and the both front and rear camera views are shown and the video automatically plays')
def verify_event_played_on_review_page():
    EVENT_REVIEW_PAGE.review_id().wait_for_expected_text(str(EVENT_REVIEW_ID))

    assert_that(EVENT_REVIEW_PAGE.back_to_home().get_text(), contains_string('arrow_back'))
    assert_that(EVENT_REVIEW_PAGE.back_to_home().get_text(), contains_string('Back to Home'))
    assert EVENT_REVIEW_PAGE.review_id_title().get_text() == 'Review ID:'
    assert EVENT_REVIEW_PAGE.review_id().get_text() == str(EVENT_REVIEW_ID)
    assert EVENT_REVIEW_PAGE.trigger_title().get_text() == 'Trigger:'
    assert EVENT_REVIEW_PAGE.record_date_title().get_text() == 'Record Date:'
    assert EVENT_REVIEW_PAGE.vehicle_id_title().get_text() == 'Vehicle ID:'
    assert EVENT_REVIEW_PAGE.vehicle_type_title().get_text() == 'Vehicle Type:'
    assert EVENT_REVIEW_PAGE.seatbelt_title().get_text() == 'Seatbelt:'
    assert EVENT_REVIEW_PAGE.audio_title().get_text() == 'Audio:'
    assert EVENT_REVIEW_PAGE.FPS_title().get_text() == 'FPS:'
    assert EVENT_REVIEW_PAGE.event_details_text().get_text() == 'Event Details'
    assert EVENT_REVIEW_PAGE.rear_view_text().get_text() == 'REAR VIEW'
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'

    event_play_time = EVENT_REVIEW_PAGE.event_play_time().get_text()
    event_play_time_changed = EVENT_REVIEW_PAGE.event_play_time().wait_for_expected_text_change(event_play_time, 6)
    # the event could not be played the first time it was opened. Not reproducible manually.
    # go back to home and reopen the event as workaround
    if event_play_time == event_play_time_changed and event_play_time.startswith('-'):
        EVENT_REVIEW_PAGE.back_to_home().click()
        EVENT_LIST_PAGE.review_id_1st().click()
    if EVENT_REVIEW_PAGE.play_and_pause().get_text() == 'play_arrow':
        EVENT_REVIEW_PAGE.play_and_pause().click()
    event_play_time_changed = EVENT_REVIEW_PAGE.event_play_time().wait_for_expected_text_change(event_play_time, 10)

    assert event_play_time_changed != event_play_time

@given('the event’s outcome and event trigger are already selected and the user is under "Behaviors" tab')
def select_outcome_trigger():
    if EVENT_REVIEW_PAGE.is_tab_active(EVENT_REVIEW_PAGE.outcome_trigger_tab(), True, 2):
        OUTCOME_TRIGGER_TAB.other_radio_btn().click()

@when('the user selects one or more behaviors under "Behaviors" tab')
def select_behaviors():
    BEHAVIORS_TAB.red_light_checkbox().click()

@then('the behaviors are selected with blue check icon')
def verify_behaviors_selected():
    assert BEHAVIORS_TAB.is_checkbox_checked(BEHAVIORS_TAB.red_light_checkbox()) is True

@when('the user clicks "Comments" button at bottom right')
def go_to_comments_tab():
    BEHAVIORS_TAB.comments().click()

@then("the user is navigated to event's 'Comments' tab")
def verify_go_to_comments_tab():
    assert EVENT_REVIEW_PAGE.is_tab_active(EVENT_REVIEW_PAGE.comments_tab(), True) is True

@when('the user selects some behaviors and the user clicks "Complete & Next" button in "Comments" tab')
def complete_review():
    COMMENTS_TAB.complete_next().click()
    sleep(100) # Wait some time for the task creation(usually it less than 60s).

@then('the event is disappeared from events list')
def verify_event_is_reviewed():
    assert EVENT_LIST_PAGE.search_range_and_results().get_text() == '0 results'

@then('the event status is updated accordingly to F2F in WS and the corresponding task is generated correctly to Due for Coaching task in WS')
def verify_event_status_and_task(browser):
    browser.get(DC_URL)
    WS_LOGIN_PAGE.user_name().type(ERD.coach_user_name)
    WS_LOGIN_PAGE.password().type(ERD.coach_password)
    WS_LOGIN_PAGE.login().click()
    WS_LOGIN_PAGE.retry_if_login_failed(ERD.coach_user_name, ERD.coach_password)

    WS_TASK_PAGE.task_navigator().click()
    WS_TASK_PAGE.due_for_coaching().click()
    WS_TASK_PAGE.search_driver().clear()
    WS_TASK_PAGE.search_driver().type(ERD.driver_employee_id)
    sleep(3)

    assert_that(WS_TASK_PAGE.coach_button().get_text(), contains_string('Coach'))
    assert_that(WS_TASK_PAGE.coach_button().get_text(), contains_string('Event'))

@then('the event score is updated correctly in WS and the behavior/trigger are displayed correctly in WS')
def verify_event_score_and_behaviors():
    coach_event_text = WS_TASK_PAGE.coach_button().get_text()
    WS_TASK_PAGE.coach_button().click()
    if coach_event_text == 'Coach Event':
        WS_TASK_PAGE.play_event().click()
    else:
        WS_TASK_PAGE.click_last_event()

    behavior_list = WS_TASK_PAGE.behaviors_list()

    assert ERD.f2f_behavior_1st in behavior_list
    assert WS_TASK_PAGE.event_id().get_text() == str(EVENT_ID)
    assert WS_TASK_PAGE.event_status().get_text() == 'Face-To-Face'

    # select action plan if company enable it
    try:
        WS_TASK_PAGE.first_action_plan().click()
    except TimeoutException:
        sleep(0.1)
    WS_TASK_PAGE.complete_session().click()
    WS_TASK_PAGE.confirm_complete().click()

#@LQ-28556
@given('the user is in the Login page of New ARC & a user has "Reviewer" role')
def login_page(browser):
    global DATA_MGR, LOGIN_PAGE, EVENT_LIST_PAGE, EVENT_REVIEW_PAGE, OUTCOME_TRIGGER_TAB, BEHAVIORS_TAB, COMMENTS_TAB, \
        WS_LOGIN_PAGE, WS_TASK_PAGE, ERD

    DATA_MGR = AutomationDataManager()
    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)
    EVENT_REVIEW_PAGE = EventReviewPage(browser)
    OUTCOME_TRIGGER_TAB = OutcomeTriggerTab(browser)
    BEHAVIORS_TAB = BehaviorsTab(browser)
    COMMENTS_TAB = CommentsTab(browser)
    WS_LOGIN_PAGE = WSLoginPage(browser)
    WS_TASK_PAGE = WSTaskPage(browser)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD

    browser.get(ARC_URL)
    sleep(5)

@when('the user clicks the Sign in button & the user select "Trainee" role in the Role dropdown list & the user select one company in the company dropdown list')
def trainee_sign_in():
    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.login().click()
    LOGIN_PAGE.role_list_trainee().click()
    LOGIN_PAGE.search_company().wait_for_element_displayed()
    LOGIN_PAGE.select_role().click()
    LOGIN_PAGE.select_reviewer_role().click()
    LOGIN_PAGE.search_company().type_and_auto_search(ERD.company_name_switch)
    LOGIN_PAGE.first_company().click()
    LOGIN_PAGE.select_company().click()

@then('the Review Center page in training mode is opened')
def verify_trainee_mode():
    assert EVENT_LIST_PAGE.title().get_text() == 'Lytx ReviewCenter'
    assert EVENT_LIST_PAGE.company_name().get_text() == ERD.company_name
    assert EVENT_LIST_PAGE.switch_company().get_text() == 'Switch Companies'
    assert EVENT_LIST_PAGE.training_mode().get_text() == 'Training Mode'
    assert EVENT_LIST_PAGE.give_feedback().get_text() == 'Give Feedback'
    assert EVENT_LIST_PAGE.new_tab().get_text() == 'New (0)'
    assert EVENT_LIST_PAGE.return_tab().get_text() == 'Returned (0)'
    assert EVENT_LIST_PAGE.review_id_filter().get_text() == 'REVIEW ID'
    assert EVENT_LIST_PAGE.filter_button().get_text() == 'Filter'
    assert EVENT_LIST_PAGE.clear_button().get_text() == 'Clear'