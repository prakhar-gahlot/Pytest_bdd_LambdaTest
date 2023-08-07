from Pages.base_page import BasePage
from Elements.button import Button
from Elements.text_box import TextBox
from Elements.label import Label
from Pages.Arc.event_review_page_locator import EventReviewPageLocator as ERP
from selenium.webdriver.common.by import By


class EventReviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # top info
    def back_to_home(self):
        return Label(self.driver, (By.XPATH, ERP.back_to_home_xpath))

    def review_id_title(self):
        return Label(self.driver, (By.XPATH, ERP.review_id_title_xpath))

    def review_id(self):
        return Label(self.driver, (By.XPATH, ERP.review_id_xpath))

    def trigger_title(self):
        return Label(self.driver, (By.XPATH, ERP.trigger_title_xpath))

    def trigger(self):
        return Label(self.driver, (By.XPATH, ERP.trigger_xpath))

    def record_date_title(self):
        return Label(self.driver, (By.XPATH, ERP.record_date_title_xpath))

    def record_date(self):
        return Label(self.driver, (By.XPATH, ERP.record_date_xpath))

    def vehicle_id_title(self):
        return Label(self.driver, (By.XPATH, ERP.vehicle_id_title_xpath))

    def vehicle_id(self):
        return Label(self.driver, (By.XPATH, ERP.vehicle_id_xpath))

    def vehicle_type_title(self):
        return Label(self.driver, (By.XPATH, ERP.vehicle_type_title_xpath))

    def vehicle_type(self):
        return Label(self.driver, (By.XPATH, ERP.vehicle_type_xpath))

    def seatbelt_title(self):
        return Label(self.driver, (By.XPATH, ERP.seatbelt_title_xpath))

    def seatbelt(self):
        return Label(self.driver, (By.XPATH, ERP.seatbelt_xpath))

    def audio_title(self):
        return Label(self.driver, (By.XPATH, ERP.audio_title_xpath))

    def audio(self):
        return Label(self.driver, (By.XPATH, ERP.audio_xpath))

    def FPS_title(self):
        return Label(self.driver, (By.XPATH, ERP.FPS_title_xpath))

    def FPS(self):
        return Label(self.driver, (By.XPATH, ERP.FPS_xpath))

    def event_details_icon(self):
        return Button(self.driver, (By.XPATH, ERP.event_details_icon_xpath))

    def event_details_text(self):
        return Label(self.driver, (By.XPATH, ERP.event_details_text_xpath))

    # event play
    def rear_view_text(self):
        return Label(self.driver, (By.XPATH, ERP.rear_view_text_xpath))

    def front_view_text(self):
        return Label(self.driver, (By.XPATH, ERP.front_view_text_xpath))

    def event_play_time(self):
        return Label(self.driver, (By.ID, ERP.event_play_time_id))

    # event review tabs
    def outcome_trigger_tab(self):
        return Button(self.driver, (By.XPATH, ERP.outcome_trigger_tab_xpath))

    def behavior_tab(self):
        return Button(self.driver, (By.XPATH, ERP.behavior_tab_xpath))

    def comments_tab(self):
        return Button(self.driver, (By.XPATH, ERP.comments_tab_xpath))

    # non-element methods
    def is_tab_active(self, tab):
        if 'mat-tab-label-active' in tab.get_attribute('class'):
            return True
        return False

    def is_checkbox_checked(self, tab):
        if 'mat-checkbox-checked' in tab.get_attribute('class'):
            return True
        return False
