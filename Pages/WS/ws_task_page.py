from Elements.base_element import BaseElement
from Elements.label import Label
from Pages.base_page import BasePage
from Elements.button import Button
from Elements.text_box import TextBox
from Pages.WS.ws_task_page_locator import WSTaskPageLocator as TP
from selenium.webdriver.common.by import By


class WSTaskPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # WS Task navigation
    def task_navigator(self):
        return Button(self.driver, (By.XPATH, TP.task_xpath))
    
    def due_for_coaching(self):
        return Button(self.driver, (By.XPATH, TP.due_for_coaching_xpath))

    # due for coaching page
    def search_driver(self):
        return TextBox(self.driver, (By.XPATH, TP.search_driver_xpath))
    
    def coach_button(self):
        return Button(self.driver, (By.XPATH, TP.coach_button_xpath))

    # coaching session page
    def play_event(self):
        return Button(self.driver, (By.XPATH, TP.play_event_xpath))

    def behaviors(self):
        return BaseElement(self.driver, (By.XPATH, TP.behaviors_xpath))
    
    def behavior_1st(self):
        return Label(self.driver, (By.XPATH, TP.behavior_1st_xpath))
    
    def behavior_2nd(self):
        return Label(self.driver, (By.XPATH, TP.behavior_2nd_xpath))

    def event_id(self):
        return Label(self.driver, (By.ID, TP.event_id_id))

    def event_status(self):
        return Label(self.driver, (By.ID, TP.event_status_id))

    def event_trigger(self):
        return Label(self.driver, (By.ID, TP.event_trigger_id))

    def event_score(self):
        return Label(self.driver, (By.ID, TP.event_score_id))

    def complete_session(self):
        return Button(self.driver, (By.ID, TP.complete_session_id))

    def confirm_complete(self):
        return Button(self.driver, (By.ID, TP.confirm_complete_id))

    # non-element methods
    def behaviors_list(self):
        behaviors = self.behaviors()._find()
        behavior_list = []
        for element in behaviors.find_elements(By.XPATH, './*'):
            behavior_list.append(element.text)

        return behavior_list
