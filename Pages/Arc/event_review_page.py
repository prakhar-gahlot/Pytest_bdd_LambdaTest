from time import sleep
from Pages.base_page import BasePage
from Elements.button import Button
from Elements.base_element import BaseElement
from Elements.label import Label
from Pages.Arc.event_review_page_locator import EventReviewPageLocator as ERP
from selenium.webdriver.common.by import By


class EventReviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # top bar
    def top_bar_title(self):
        return Label(self.driver, (By.CLASS_NAME, ERP.top_bar_title_class_name))

    def top_bar_review_text(self):
        return Label(self.driver, (By.CLASS_NAME, ERP.top_bar_review_text_class_name))

    def top_bar_switch_company(self):
        return Label(self.driver, (By.CLASS_NAME, ERP.top_bar_switch_company_class_name))

    # video
    def video(self):
        return BaseElement(self.driver, (By.TAG_NAME, ERP.video_tag_name))

    # top info
    def back_to_home(self):
        return Button(self.driver, (By.XPATH, ERP.back_to_home_xpath))

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

    def play_and_pause(self):
        return Button(self.driver, (By.XPATH, ERP.play_and_pause_xpath))

    def rear_and_front(self):
        return Button(self.driver, (By.CLASS_NAME, ERP.rear_and_front_class_name))

    def rear(self):
        return Button(self.driver, (By.CLASS_NAME, ERP.rear_class_name))

    def front(self):
        return Button(self.driver, (By.CLASS_NAME, ERP.front_class_name))

    def backward(self):
        return Button(self.driver, (By.XPATH, ERP.backward_xpath))

    def forward(self):
        return Button(self.driver, (By.XPATH, ERP.forward_xpath))

    def backward_1(self):
        return Button(self.driver, (By.XPATH, ERP.backward_1_xpath))

    def forward_1(self):
        return Button(self.driver, (By.XPATH, ERP.forward_1_xpath))

    def full_screen(self):
        return Button(self.driver, (By.CLASS_NAME, ERP.full_screen_class_name))

    def stop_watch(self):
        return Button(self.driver, (By.CLASS_NAME, ERP.stop_watch_class_name))

    # telemetry bar
    def telemetry_graph(self):
        return BaseElement(self.driver, (By.TAG_NAME, ERP.telemetry_graph_tab_name))

    def scrubber(self):
        return BaseElement(self.driver, (By.ID, ERP.scrubber_id))

    def current_time(self):
        return Button(self.driver, (By.ID, ERP.current_time_id))

    def fwd(self):
        return Label(self.driver, (By.ID, ERP.fwd_id))

    def lat(self):
        return Label(self.driver, (By.ID, ERP.lat_id))

    def time(self):
        return Label(self.driver, (By.ID, ERP.time_id))

    def gps_speed(self):
        return Label(self.driver, (By.ID, ERP.gps_speed_id))

    def fwd_force_graph(self):
        return Label(self.driver, (By.XPATH, ERP.fwd_force_graph_xpath))

    def lat_force_graph(self):
        return Label(self.driver, (By.XPATH, ERP.lat_force_graph_xpath))

    def gps_speed_force_graph(self):
        return Label(self.driver, (By.XPATH, ERP.gps_speed_force_graph_xpath))

    def time_force_graph(self):
        return Label(self.driver, (By.XPATH, ERP.time_force_graph_xpath))


    # event review tabs
    def outcome_trigger_tab(self):
        return Button(self.driver, (By.XPATH, ERP.outcome_trigger_tab_xpath))

    def behavior_tab(self):
        return Button(self.driver, (By.XPATH, ERP.behavior_tab_xpath))

    def comments_tab(self):
        return Button(self.driver, (By.XPATH, ERP.comments_tab_xpath))

    # non-element methods
    def is_tab_active(self, tab, expected_value, attempts=10):
        n = 0
        while n < attempts:
            n += 1
            if ('mat-tab-label-active' in tab.get_attribute('class')) == expected_value:
                return expected_value
            sleep(3)

        return ('mat-tab-label-active' in tab.get_attribute('class'))

    def is_checkbox_checked(self, tab):
        if 'mat-checkbox-checked' in tab.get_attribute('class'):
            return True
        return False

    def is_button_active(self, btn):
        if 'active' in btn.get_attribute('class'):
            return True
        return False
