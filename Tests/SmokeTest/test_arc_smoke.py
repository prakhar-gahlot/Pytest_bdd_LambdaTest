from pytest_bdd import scenarios, given, when, then
from Pages.Arc.event_list_page import EventListPage
from Pages.Arc.login_page import LoginPage
from Tests.common import DC_URL, ENV
from TestingData.Int.event_review_data_int import EventReviewDataInt as ERD_INT


LOGIN_PAGE = 0
EVENT_LIST_PAGE = 0
ERD = ''

scenarios('Features/Smoke/arc_smoke.feature')


# LQ-263
@given('the user is in the Login page of New ARC and a user has Reviewer role in some companies')
def open_login_page(browser):
    global LOGIN_PAGE, EVENT_LIST_PAGE, ERD

    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_INT
    else:
        ERD = ERD_INT

@when('the user inputs valid username and password and the user clicks the Sign in button')
def reviewer_sign_in():
    LOGIN_PAGE.user_name.type(ERD.coach_user_name)
    LOGIN_PAGE.password.type(ERD.password)

    LOGIN_PAGE.login.click()

@when('the user select Reviewer role in the Role dropdown list and the user select one company in the company dropdown list and the user clicks the Select button')
def reviewer_select_role_and_company():
    LOGIN_PAGE.search_company.type(ERD.company_name)
    LOGIN_PAGE.first_company.click()
    LOGIN_PAGE.select_company.click()

    LOGIN_PAGE.click_login()

@then('the Review page is opened')
def verify_event_list_page_opened():
    assert EventListPage.title().get_text == 'Lytx ReviewCenter'
