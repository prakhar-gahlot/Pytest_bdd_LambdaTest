from Elements.label import Label
from Pages.base_page import BasePage
from Elements.button import Button
from Elements.text_box import TextBox
from Pages.Arc.login_page_locator import LoginPageLocator as LP
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # login page elements
    def login_page_title(self):
        return Label(self.driver, (By.XPATH, LP.login_page_title_xpath))

    def user_name(self):
        return TextBox(self.driver, (By.XPATH, LP.user_name_xpath))

    def password(self):
        return TextBox(self.driver, (By.XPATH, LP.password_xpath))

    def login(self):
        return Button(self.driver, (By.XPATH, LP.login_xpath))

    def login_error_text(self):
        return Label(self.driver, (By.XPATH, LP.login_error_xpath))

    def role_list_first(self):
        return Button(self.driver, (By.XPATH, LP.role_list_first_xpath))

    def role_list_trainee(self):
        return Button(self.driver, (By.XPATH, LP.role_trainee_xpath))

    # select company page elements
    def select_role(self):
        return TextBox(self.driver, (By.XPATH, LP.select_role_xpath))

    def select_reviewer_role(self):
        return TextBox(self.driver, (By.XPATH, LP.select_reviewer_xpath))

    def search_company(self):
        return TextBox(self.driver, (By.XPATH, LP.search_company_xpath))

    def first_company(self):
        return Button(self.driver, (By.XPATH, LP.first_company_xpath))

    def second_company(self):
        return Button(self.driver, (By.XPATH, LP.second_company_xpath))

    def third_company(self):
        return Button(self.driver, (By.XPATH, LP.third_company_xpath))

    def fourth_company(self):
        return Button(self.driver, (By.XPATH, LP.fourth_company_xpath))

    def select_company(self):
        return Button(self.driver, (By.XPATH, LP.select_company_xpath))

    # combine actions
    def user_login(self, user_name, password):
        self.user_name()._type(user_name)
        self.password()._type(password)
        self.login()._click()
