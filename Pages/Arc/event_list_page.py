from Pages.base_page import BasePage
from Elements.button import Button
from Elements.text_box import TextBox
from Elements.label import Label
from Pages.Arc.event_list_page_locator import EventListPage as ELP
from selenium.webdriver.common.by import By


class EventListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # top bar
    def title(self):
        return Label(self.driver, (By.XPATH, ELP.title_xpath))

    def reviewing_company(self):
        return Label(self.driver, (By.XPATH, ELP.reviewing_company_xpath))

    def company_name(self):
        return Label(self.driver, (By.XPATH, ELP.company_name_xpath))

    def switch_company(self):
        return Button(self.driver, (By.XPATH, ELP.switch_company_xpath))

    # combine actions
