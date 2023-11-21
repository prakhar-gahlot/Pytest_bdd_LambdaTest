from Elements.label import Label
from Pages.base_page import BasePage
from Elements.button import Button
from Elements.text_box import TextBox
from Pages.WS.ws_library_page_locator import WSLibraryPageLocator as LP
from selenium.webdriver.common.by import By


class WSLibraryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # WS Library navigation
    def library_navigator(self):
        return Button(self.driver, (By.XPATH, LP.library_navigator_xpath))
    
    def events(self):
        return Button(self.driver, (By.XPATH, LP.events_xpath))

    # events page
    def select_search(self):
        return Button(self.driver, (By.ID, LP.select_search_id))
    
    def select_search_event_id(self):
        return Button(self.driver, (By.XPATH, LP.select_search_event_id_xpath))

    def select_search_criteria(self):
        return TextBox(self.driver, (By.ID, LP.select_search_criteria_id))

    def search_icon(self):
        return Button(self.driver, (By.XPATH, LP.search_icon_xpath))
    
    def event_status_1st(self):
        return Label(self.driver, (By.XPATH, LP.event_status_1st_xpath))
    
    def event_trigger_1st(self):
        return Label(self.driver, (By.XPATH, LP.event_trigger_1st_xpath))

    def event_behaviors_1st(self):
        return Label(self.driver, (By.XPATH, LP.event_behaviors_1st_xpath))

    # non-element methods
