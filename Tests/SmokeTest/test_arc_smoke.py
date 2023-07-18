from pytest_bdd import scenarios, given, when, then
from Pages.Arc.event_list_page import EventListPage
from Pages.Arc.login_page import LoginPage
from Tests.common import DC_URL, ARC_URL, ENV
from TestingData.Int.event_review_data_int import EventReviewDataInt as ERD_INT
from TestingData.Stg.event_review_data_stg import EventReviewDataStg as ERD_STG
from TestingData.Prod.event_review_data_prod import EventReviewDataProd as ERD_PROD


LOGIN_PAGE = 0
EVENT_LIST_PAGE = 0
ERD = ''

scenarios('../../Features/Smoke/arc_smoke.feature')


# LQ-9709
@given('the user is in the Login page of New ARC and a user has Reviewer role in some companies')
def open_login_page(browser):
    global LOGIN_PAGE, EVENT_LIST_PAGE, ERD

    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)

    browser.get(ARC_URL)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD

@when('the user inputs valid username and password and the user clicks the Sign in button')
def reviewer_sign_in():
    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)

    LOGIN_PAGE.login().click()

@when('the user select Reviewer role in the Role dropdown list and the user select one company in the company dropdown list and the user clicks the Select button')
def reviewer_select_role_and_company():
    LOGIN_PAGE.search_company().type(ERD.company_name)
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

    LOGIN_PAGE.search_company().type(ERD.company_name)
    LOGIN_PAGE.first_company().click()
    LOGIN_PAGE.select_company().click()

@then('"Reviewing for: Company A" text is displayed behind "Lytx ReviewerCenter" '
      'and "Switch Companies" button with clickable status is displayed behind "Reviewing for: Company A" '
      'and there is a Give Feedback link on the top-right corner')
def verify_selected_company():
    assert EVENT_LIST_PAGE.title().get_text() == 'Lytx ReviewCenter'
    assert EVENT_LIST_PAGE.company_name().get_text() == ERD.company_name
    assert EVENT_LIST_PAGE.switch_company().get_text() == 'Switch Companies'
