from Elements.button import Button
from Elements.text_box import TextBox
from Elements.label import Label
from Pages.Arc.outcome_trigger_tab_locator import OutcomeTriggerTabLocator as OTT
from Pages.Arc.event_review_page import EventReviewPage
from selenium.webdriver.common.by import By


class OutcomeTriggerTab(EventReviewPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # outcome

    # event trigger
    def other_radio_btn(self):
        return Button(self.driver, (By.XPATH, OTT.other_radio_btn_xpath))

    def other(self):
        return Label(self.driver, (By.XPATH, OTT.other_xpath))
