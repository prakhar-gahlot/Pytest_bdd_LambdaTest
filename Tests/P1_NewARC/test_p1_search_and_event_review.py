from datetime import datetime, timedelta
from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then
from Pages.Arc.behaviors_tab import BehaviorsTab
from Pages.Arc.comments_tab import CommentsTab
from Pages.Arc.event_list_page import EventListPage
from Pages.Arc.event_review_page import EventReviewPage
from Pages.Arc.login_page import LoginPage
from Pages.Arc.outcome_trigger_tab import OutcomeTriggerTab
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
EVENT_REVIEW_ID_1ST = 0
EVENT_REVIEW_ID_2ND = 0
EVENT_REVIEW_ID_3RD = 0
CUSTOM_BEHAVIORS = []
DATA_MGR = ''

scenarios('../../Features/P1_NewARC/p1_search_and_event_review.feature')


# LQ-10595
@given('the user logins to ARC')
def login_arc(browser):
    global DATA_MGR, LOGIN_PAGE, EVENT_LIST_PAGE, EVENT_REVIEW_PAGE, OUTCOME_TRIGGER_TAB, BEHAVIORS_TAB, COMMENTS_TAB, ERD

    DATA_MGR = AutomationDataManager()
    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)
    EVENT_REVIEW_PAGE = EventReviewPage(browser)
    OUTCOME_TRIGGER_TAB = OutcomeTriggerTab(browser)
    BEHAVIORS_TAB = BehaviorsTab(browser)
    COMMENTS_TAB = CommentsTab(browser)

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
def filter_event_in_new_tab():
    global EVENT_REVIEW_ID_1ST, EVENT_REVIEW_ID_2ND, EVENT_REVIEW_ID_3RD
    EVENT_REVIEW_ID_1ST = DATA_MGR.create_new_event(ERD.behavior_1st, ERD.ER_with_custom_behaviors)
    EVENT_REVIEW_ID_2ND = DATA_MGR.create_new_event(ERD.behavior_2nd, ERD.ER_with_many_custom_behaviors)
    EVENT_REVIEW_ID_3RD = DATA_MGR.create_new_event(ERD.behavior_2nd, ERD.ER_without_custom_behaviors)

    EVENT_LIST_PAGE.new_tab().click()
    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID_1ST)
    EVENT_LIST_PAGE.filter_button().click()

@then('the related event is filtered out under the New tab and the event count of New tab is shown')
def verify_new_event_filtered():
    EVENT_LIST_PAGE.search_range_and_results().wait_for_expected_text('1 result')
    creation_date = datetime.strptime(EVENT_LIST_PAGE.creation_date_1st().get_text(), '%Y-%m-%d %I:%M %p')

    assert_that(EVENT_LIST_PAGE.search_range_and_results().get_text(), contains_string(str(EVENT_REVIEW_ID_1ST)))
    assert_that(EVENT_LIST_PAGE.search_range_and_results().get_text(), contains_string('1 result'))
    assert_that(EVENT_LIST_PAGE.new_tab().get_text(), contains_string('New (1)'))
    assert EVENT_LIST_PAGE.review_id_1st().get_text() == str(EVENT_REVIEW_ID_1ST)
    assert creation_date < datetime.now()
    assert EVENT_LIST_PAGE.vehicle_name_1st().get_text() == ERD.vehicle
    assert EVENT_LIST_PAGE.serial_num_1st().get_text() == ERD.ER_with_custom_behaviors

@then('the event list shows columns: "REVIEW ID","EVENT ID","CREATION DATE","VEHICLE NAME","ER SERIAL"')
def verify_event_columns():
    assert EVENT_LIST_PAGE.review_id_title().get_text() == 'REVIEW ID'
    assert EVENT_LIST_PAGE.event_id_title().get_text() == 'EVENT ID'
    assert EVENT_LIST_PAGE.creation_date_title().get_text() == 'CREATION DATE'
    assert EVENT_LIST_PAGE.vehicle_name_title().get_text() == 'VEHICLE NAME'
    assert EVENT_LIST_PAGE.serial_num_title().get_text() == 'ER SERIAL #'

# LQ-10597
@when('the user filtered a range of Review IDs under New tab')
def filter_events_in_new_tab():
    EVENT_LIST_PAGE.review_id_filter().clear()

    review_id_range = ERD.review_id_range_from + '-' + ERD.review_id_range_to
    EVENT_LIST_PAGE.review_id_filter().type(review_id_range)
    EVENT_LIST_PAGE.filter_button().click()

@then('Review ID is displayed and the events in the range are displayed and Event ID is displayed as CustomerString ID')
def verify_new_events_filtered():
    EVENT_LIST_PAGE.search_range_and_results().wait_for_expected_text('-')
    new_tab_text = EVENT_LIST_PAGE.new_tab().get_text()
    event_count = int(new_tab_text.split('(')[1].split(')')[0])
    event_cust_id = EVENT_LIST_PAGE.event_id_1st().get_text()
    event_cust_id_prefix = event_cust_id[3]
    event_cust_id_suffix = event_cust_id[-5]

    assert EVENT_LIST_PAGE.get_row_count() == event_count
    assert event_count > 0
    assert EVENT_LIST_PAGE.review_id_1st().get_text() >= ERD.review_id_range_from
    assert EVENT_LIST_PAGE.review_id_1st().get_text() <= ERD.review_id_range_to
    assert len(event_cust_id) == 9
    assert event_cust_id_suffix.isdigit() is True
    for i in event_cust_id_prefix:
        assert i.isalpha() is True

@then('Creation Date is event creation date based on local time zone and displayed as format YYYY-MM-DD hh:mm AM/PM')
def verify_new_events_creation_date():
    creation_date = datetime.strptime(EVENT_LIST_PAGE.creation_date_1st().get_text(), '%Y-%m-%d %I:%M %p')

    assert creation_date < datetime.now()
    assert creation_date > datetime.strptime('2020-01-01 1:01 AM', '%Y-%m-%d %I:%M %p')

@then('Vehicle Name is displayed correctly and ER Serial is displayed correctly')
def verify_new_events_vehicle_ER():
    assert len(EVENT_LIST_PAGE.vehicle_name_1st().get_text()) > 0
    assert len(EVENT_LIST_PAGE.serial_num_1st().get_text()) > 0

@when('the user input Review ID range and Clicks Filter button in New tab')
def filter_events_in_new_tab():
    range = str(EVENT_REVIEW_ID_1ST) + '-' + str(EVENT_REVIEW_ID_3RD)
    EVENT_LIST_PAGE.review_id_filter().clear()
    EVENT_LIST_PAGE.review_id_filter().type(range)
    EVENT_LIST_PAGE.filter_button().click()

@then('the result of filtered new events is displayed above event list')
def verify_filtered_result_events():
    assert EVENT_LIST_PAGE.search_range_and_results().wait_for_expected_text(str(EVENT_REVIEW_ID_3RD)) == str(EVENT_REVIEW_ID_1ST) + '-' + str(EVENT_REVIEW_ID_3RD) + ' • 3 results'

@when('the user input Review ID and Clicks Filter button in New tab')
def filter_single_event_in_new_tab():
    EVENT_LIST_PAGE.review_id_filter().clear()
    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID_3RD)
    EVENT_LIST_PAGE.filter_button().click()

@then('the result of filtered single event is displayed above event list')
def verify_filtered_result_single_event():
    assert EVENT_LIST_PAGE.search_range_and_results().wait_for_expected_text(str(EVENT_REVIEW_ID_3RD)) == str(EVENT_REVIEW_ID_3RD) + ' • 1 result'

# LQ-11154
@when('the user clicks one reviewID in a group which has no enabled custom behavior and the user opens the Behavior tab and the user clicks "More Behaviors >" button')
def open_event_without_custom_behaviors():
    EVENT_LIST_PAGE.review_id_1st().click()
    if OUTCOME_TRIGGER_TAB.other_radio_btn().wait_for_element_is_clickable() is False:
        EVENT_REVIEW_PAGE.back_to_home().click()
        EVENT_LIST_PAGE.review_id_1st().click()
    OUTCOME_TRIGGER_TAB.other_radio_btn().click()
    BEHAVIORS_TAB.more_behaviors().click()

@then('the Custom Behaviors section is not displayed')
def verify_event_without_custom_behaviors():
    assert BEHAVIORS_TAB.custom_behaviors_title().element_is_displayed() is False

@when('the user clicks one reviewID in a group which has some enabled custom behaviors includes MVAI behaviors and the user opens the Behavior tab and the user clicks "More Behaviors >" button')
def open_event_with_custom_and_mvai_behaviors():
    EVENT_REVIEW_PAGE.back_to_home().click()
    EVENT_LIST_PAGE.review_id_filter().clear()
    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID_1ST)
    EVENT_LIST_PAGE.filter_button().click()
    EVENT_LIST_PAGE.review_id_1st().click()
    if OUTCOME_TRIGGER_TAB.other_radio_btn().wait_for_element_is_clickable() is False:
        EVENT_REVIEW_PAGE.back_to_home().click()
        EVENT_LIST_PAGE.review_id_1st().click()
    OUTCOME_TRIGGER_TAB.other_radio_btn().click()
    BEHAVIORS_TAB.more_behaviors().click()

@then('the Custom Behaviors section is displayed with all enabled custom behaviors and the MVAI custom behaviors are not visible for the "Reviewer" user')
def verify_event_with_custom_and_mvai_behaviors():
    assert BEHAVIORS_TAB.custom_behaviors_title().element_is_displayed() is True

@when('the user clicks one reviewID in a group which has lots of enabled custom behaviors and the user opens the Behavior tab and the user clicks "More Behaviors >" button')
def open_event_with_lots_of_custom_behaviors():
    EVENT_REVIEW_PAGE.back_to_home().click()
    EVENT_LIST_PAGE.review_id_filter().clear()
    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID_2ND)
    EVENT_LIST_PAGE.filter_button().click()
    EVENT_LIST_PAGE.review_id_1st().click()
    if OUTCOME_TRIGGER_TAB.other_radio_btn().wait_for_element_is_clickable() is False:
        EVENT_REVIEW_PAGE.back_to_home().click()
        EVENT_LIST_PAGE.review_id_1st().click()
    OUTCOME_TRIGGER_TAB.other_radio_btn().click()
    BEHAVIORS_TAB.more_behaviors().click()

@then('the Custom Behaviors section is displayed with all enabled custom behaviors')
def verify_event_with_lots_of_custom_behaviors():
    assert BEHAVIORS_TAB.custom_behaviors_title().element_is_displayed() is True
    assert len(BEHAVIORS_TAB.custom_behaviors()) > 8
    assert BEHAVIORS_TAB.the_9th_custom_behavior().element_is_displayed() is True

@when('the user clicks one reviewID in a group which has different enabled custom behaviors and the user opens the Behavior tab and the user clicks "More Behaviors >" button')
def open_event_with_different_custom_behaviors():
    global CUSTOM_BEHAVIORS
    CUSTOM_BEHAVIORS = BEHAVIORS_TAB.custom_behaviors()

    EVENT_REVIEW_PAGE.back_to_home().click()
    EVENT_LIST_PAGE.review_id_filter().clear()
    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID_1ST)
    EVENT_LIST_PAGE.filter_button().click()
    EVENT_LIST_PAGE.review_id_1st().click()
    if OUTCOME_TRIGGER_TAB.other_radio_btn().wait_for_element_is_clickable() is False:
        EVENT_REVIEW_PAGE.back_to_home().click()
        EVENT_LIST_PAGE.review_id_1st().click()
    OUTCOME_TRIGGER_TAB.other_radio_btn().click()
    BEHAVIORS_TAB.more_behaviors().click()

@then('the custom behavior listed in the event is different from the behaviors listed in the previous event')
def verify_event_with_different_custom_behaviors():
    different_behaviors = BEHAVIORS_TAB.custom_behaviors()
    count = len(different_behaviors) if len(different_behaviors) <= len(CUSTOM_BEHAVIORS) else len(CUSTOM_BEHAVIORS)
    i = 0
    is_same = True
    while i < count:
        if CUSTOM_BEHAVIORS[i] != different_behaviors[i]:
            is_same = False
        i += 1

    assert BEHAVIORS_TAB.custom_behaviors_title().element_is_displayed() is True
    assert len(different_behaviors) > 0
    assert is_same is False

@when('the user clicks one reviewID and opens the Behavior tab and the user clicks "More Behaviors >" button and the user checks all custom behaviors and the user clicks "Comments" button')
def open_event_and_select_custom_behaviors_and_go_to_comments():
    global CUSTOM_BEHAVIORS
    CUSTOM_BEHAVIORS = BEHAVIORS_TAB.custom_behaviors()

    BEHAVIORS_TAB.select_all_custom_behaviors()
    BEHAVIORS_TAB.comments().click()

@then('the comments of selected custom behaviors are listed')
def verify_custom_behaviors_in_comments():
    behavior_list = COMMENTS_TAB.behaviors()
    comment_list = COMMENTS_TAB.behavior_comments()

    assert behavior_list == ERD.custom_behaviors
    assert comment_list == ERD.custom_behavior_comments
