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

    def password_masked(self):
        return TextBox(self.driver, (By.XPATH, LP.password_masked_xpath))

    def login(self):
        return Button(self.driver, (By.XPATH, LP.login_xpath))

    def login_error_text(self):
        return Label(self.driver, (By.XPATH, LP.login_error_xpath))

    # select company page elements
    def select_role(self):
        return Label(self.driver, (By.ID, LP.select_role_id))

    def search_company(self):
        return TextBox(self.driver, (By.ID, LP.search_company_id))

    def first_company(self):
        return Button(self.driver, (By.ID, LP.first_company_id))

    def select_company(self):
        return Button(self.driver, (By.XPATH, LP.select_company_xpath))

    # combine actions
    def user_login(self, user_name, password):
        self.user_name()._type(user_name)
        self.password()._type(password)
        self.login()._click()
