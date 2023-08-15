from Elements.base_element import BaseElement
from Pages.base_page import BasePage
from Elements.button import Button
from Elements.text_box import TextBox
from Pages.WS.ws_login_page_locator import WSLoginPageLocator as LP
from selenium.webdriver.common.by import By
from Tests.common import DC_URL


class WSLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # login page elements
    def user_name(self):
        return TextBox(self.driver, (By.ID, LP.username_id))

    def password(self):
        return TextBox(self.driver, (By.ID, LP.password_id))

    def login(self):
        return Button(self.driver, (By.ID, LP.login_id))

    def login_success_lytx_logo(self):
        return BaseElement(self.driver, (By.XPATH, LP.login_success_lytx_logo_dc_xpath))

    # other combined methods
    def retry_if_login_failed(self, user_name, password):
        if not self.login_success_lytx_logo().wait_for_element_displayed(2):
            self.driver.get(DC_URL)
            self.user_name().type(user_name)
            self.password().type(password)
            self.login().click()
