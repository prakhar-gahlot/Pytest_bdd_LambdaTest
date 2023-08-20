from pytest_bdd import scenarios, given, when, then
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

scenarios('../../Features/P1_NewARC/p1_login.feature')


# LQ-9701
@given('the login page of New ARC is opened')
def open_login_page(browser):
    global LOGIN_PAGE, EVENT_LIST_PAGE, EVENT_REVIEW_PAGE, OUTCOME_TRIGGER_TAB, BEHAVIORS_TAB, ERD

    LOGIN_PAGE = LoginPage(browser)

    browser.get(ARC_URL)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD


@when('the user only inputs some characters in the username input box')
def enter_username_only():
    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)


@then('the Sign in button is disabled')
def verify_sign_in_button():
    assert LOGIN_PAGE.login().get_state() is False


@when('the user only inputs some characters in the password input box')
def enter_password_only():
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.user_name().remove_text()


@then('the Sign in button is disabled')
def verify_sign_in_button():
    assert LOGIN_PAGE.login().get_state() is False


@when('the user inputs some characters in the username and password input box')
def reviewer_sign_in():
    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)


@then('the Sign in button is enabled, the characters in the username are displayed as the entered characters and'
      ' encrypted characters in the password are displayed as some dots')
def reviewer_sign_in():
    assert LOGIN_PAGE.login().get_state() is True
    assert LOGIN_PAGE.user_name().get_attribute('value') == ERD.reviewer_user_name
    assert LOGIN_PAGE.password_masked().wait_for_element_displayed() is True


@when('the user clears the characters in the username and password input box')
def clear_login_credentails():
    LOGIN_PAGE.user_name().remove_text()
    LOGIN_PAGE.password().remove_text()


@then('the Sign in button is disabled')
def verify_sign_in_button():
    assert LOGIN_PAGE.login().get_state() is False


# LQ-9702
@when('the user inputs a invalid username and valid password for reviewer role')
def invalid_username():
    LOGIN_PAGE.user_name().type(LOGIN_PAGE.get_random_str(5))
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.login().click()


@then('the message "Incorrect username or password. Try again." shows below the Password input box')
def verify_sign_in_error():
    assert LOGIN_PAGE.login_error_text().get_text() == 'Incorrect username or password. Try again.'


@when('the user inputs a valid username and invalid password for reviewer role')
def invalid_password():
    LOGIN_PAGE.user_name().remove_text()
    LOGIN_PAGE.password().remove_text()
    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(LOGIN_PAGE.get_random_str(5))
    LOGIN_PAGE.login().click()


@then('the message "Incorrect username or password. Try again." shows below the Password input box')
def verify_sign_in_error():
    assert LOGIN_PAGE.login_error_text().get_text() == 'Incorrect username or password. Try again.'


# LQ-9700
@then(
    'The title is "Lytx ReviewCenter" displayed with a dark background, Username input box is displayed with watermark "Username", Password input box is displayed with watermark "Password" and "Sign in" button is disabled as default')
def reviewer_sign_in():
    LOGIN_PAGE.user_name().remove_text()
    LOGIN_PAGE.password().remove_text()
    assert LOGIN_PAGE.login_page_title().get_text() == 'Lytx ReviewCenter'
    assert LOGIN_PAGE.user_name().get_attribute('placeholder') == 'Username'
    assert LOGIN_PAGE.password().get_attribute('placeholder') == 'Password'
    assert LOGIN_PAGE.login().get_state() is False


# LQ-9704
@when('the user inputs valid username and password and the user clicks the Sign in button')
def reviewer_sign_in():
    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.login().click()


@then('the user login successfully, the role and company selection page is opened')
def select_role_company_page():
    assert LOGIN_PAGE.select_role().get_text() == 'Reviewer'
    assert LOGIN_PAGE.search_company().get_attribute('placeholder') == 'Select Company'
