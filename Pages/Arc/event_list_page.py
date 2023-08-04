from Pages.base_page import BasePage
from Elements.button import Button
from Elements.text_box import TextBox
from Elements.label import Label
from Pages.Arc.event_list_page_locator import EventListPageLocator as ELP
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

    def give_feedback(self):
        return Button(self.driver, (By.XPATH, ELP.give_feedback_xpath))

    # switch company dialog
    def search_company_switch_company(self):
        return TextBox(self.driver, (By.XPATH, ELP.search_company_switch_company_xpath))

    def first_company(self):
        return Button(self.driver, (By.XPATH, ELP.first_company_xpath))

    def select_company(self):
        return Button(self.driver, (By.XPATH, ELP.select_company_xpath))

    # filter and tabs
    def review_id_filter(self):
        return TextBox(self.driver, (By.XPATH, ELP.review_id_filter_xpath))

    def filter_button(self):
        return Button(self.driver, (By.XPATH, ELP.filter_button_xpath))

    def clear_button(self):
        return Button(self.driver, (By.XPATH, ELP.clear_button_xpath))

    def new_tab(self):
        return Button(self.driver, (By.XPATH, ELP.new_tab_xpath))

    def return_tab(self):
        return Button(self.driver, (By.XPATH, ELP.return_tab_xpath))

    def search_range_and_results(self):
        return TextBox(self.driver, (By.XPATH, ELP.search_range_and_results_xpath))

    # event list titles
    def review_id_title(self):
        return TextBox(self.driver, (By.XPATH, ELP.review_id_title_xpath))

    def event_id_title(self):
        return TextBox(self.driver, (By.XPATH, ELP.event_id_title_xpath))

    def creation_date_title(self):
        return TextBox(self.driver, (By.XPATH, ELP.creation_date_title_xpath))

    def vehicle_name_title(self):
        return TextBox(self.driver, (By.XPATH, ELP.vehicle_name_title_xpath))

    def serial_num_title(self):
        return TextBox(self.driver, (By.XPATH, ELP.serial_num_title_xpath))

    # event list first row if only one event returned
    def review_id_1st_only(self):
        return Button(self.driver, (By.XPATH, ELP.review_id_1st_only_xpath))

    def event_id_1st_only(self):
        return TextBox(self.driver, (By.XPATH, ELP.event_id_1st_only_xpath))

    def creation_date_1st_only(self):
        return TextBox(self.driver, (By.XPATH, ELP.creation_date_1st_only_xpath))

    def vehicle_name_1st_only(self):
        return TextBox(self.driver, (By.XPATH, ELP.vehicle_name_1st_only_xpath))

    def serial_num_1st_only(self):
        return TextBox(self.driver, (By.XPATH, ELP.serial_num_1st_only_xpath))

    # event list rows if multiple events returned
    def review_id_1st(self):
        return Button(self.driver, (By.XPATH, ELP.review_id_1st_xpath))

    def event_id_1st(self):
        return TextBox(self.driver, (By.XPATH, ELP.event_id_1st_xpath))

    def creation_date_1st(self):
        return TextBox(self.driver, (By.XPATH, ELP.creation_date_1st_xpath))

    def vehicle_name_1st(self):
        return TextBox(self.driver, (By.XPATH, ELP.vehicle_name_1st_xpath))

    def serial_num_1st(self):
        return TextBox(self.driver, (By.XPATH, ELP.serial_num_1st_xpath))

    # combine actions
