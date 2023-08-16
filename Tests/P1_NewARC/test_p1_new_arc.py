from pytest_bdd import scenarios, given, when, then
from Pages.Arc.event_list_page import EventListPage
from Pages.Arc.event_review_page import EventReviewPage
from Pages.Arc.outcome_trigger_tab import OutcomeTriggerTab
from Pages.Arc.behaviors_tab import BehaviorsTab
from Pages.Arc.login_page import LoginPage
from Tests.common import ARC_URL, ENV
from TestingData.Int.event_review_data_int import EventReviewDataInt as ERD_INT
from TestingData.Stg.event_review_data_stg import EventReviewDataStg as ERD_STG
from TestingData.Prod.event_review_data_prod import EventReviewDataProd as ERD_PROD


LOGIN_PAGE = 0
EVENT_LIST_PAGE = 0
EVENT_REVIEW_PAGE = 0
OUTCOME_TRIGGER_TAB = 0
BEHAVIORS_TAB = 0
ERD = ''
EVENT_REVIEW_ID = 0

scenarios('../../Features/P1_NewARC/p1_new_arc.feature')


# LQ-9700
@given('the user opens the URL of New ARC')
def open_login_page(browser):
    global LOGIN_PAGE, EVENT_LIST_PAGE, EVENT_REVIEW_PAGE, OUTCOME_TRIGGER_TAB, BEHAVIORS_TAB, ERD

    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)
    EVENT_REVIEW_PAGE = EventReviewPage(browser)
    OUTCOME_TRIGGER_TAB = OutcomeTriggerTab(browser)
    BEHAVIORS_TAB = BehaviorsTab(browser)

    browser.get(ARC_URL)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD

@then('the login page of New ARC is opened. The title is "Lytx ReviewCenter" displayed with a dark background and Username input box is displayed with watermark "Username" and Password input box is displayed with watermark "Password" and "Sign in" button is disabled as default')
def reviewer_sign_in_page():
    assert LOGIN_PAGE.user_name().get_attribute('placeholder') == 'Username'
    assert LOGIN_PAGE.password().get_attribute('placeholder') == 'Password'
    assert LOGIN_PAGE.login_page_title().get_text() == 'Lytx ReviewCenter'
    assert LOGIN_PAGE.login().get_state() is False

# LQ-9704
@when('the user inputs valid username and password and the user clicks the Sign in button')
def reviewer_sign_in():
    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.login().click()

@then('the user login successfully, the role and company selection page is opened')
def verify_event_list_page_opened():
    assert LOGIN_PAGE.select_role().get_text() == 'Reviewer'
    assert LOGIN_PAGE.search_company().get_attribute('placeholder') == 'Select Company'
