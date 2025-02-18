from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Elements.button import Button
from Elements.text_box import TextBox
from Elements.label import Label
from Pages.Arc.behaviors_tab_locator import BehaviorsTabLocator as BTL
from Pages.Arc.event_review_page import EventReviewPage
from selenium.webdriver.common.by import By


class BehaviorsTab(EventReviewPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # comments and more behaviors button
    def comments(self):
        return Button(self.driver, (By.CLASS_NAME, BTL.comments_class))

    def comments_more_behaviors(self):
        return Button(self.driver, (By.CLASS_NAME, BTL.comments_more_behaviors_class))

    def more_behaviors(self):
        return Button(self.driver, (By.XPATH, BTL.more_behaviors_xpath))

    def previous_behaviors(self):
        return Button(self.driver, (By.XPATH, BTL.previous_behaviors_xpath))

    # Distractions

    # Awareness
    def blank_stare_checkbox(self):
        return Button(self.driver, (By.XPATH, BTL.blank_stare_checkbox_xpath))

    def blank_stare(self):
        return Label(self.driver, (By.XPATH, BTL.blank_stare_xpath))

    # Fundamentals

    # Following Distance

    # Traffic Violations
    def red_light_checkbox(self):
        return Button(self.driver, (By.XPATH, BTL.red_light_checkbox_xpath))

    def red_light(self):
        return Label(self.driver, (By.XPATH, BTL.red_light_xpath))

    # Driver Condition

    # Driver Conduct
    def falling_asleep_checkbox(self):
        return Button(self.driver, (By.XPATH, BTL.falling_asleep_checkbox_xpath))

    def falling_asleep(self):
        return Label(self.driver, (By.XPATH, BTL.falling_asleep_xpath))

    # Other Behaviors

    # Driver Un-belted

    # Custom Behaviors
    def custom_behaviors_title(self):
        return Label(self.driver, (By.XPATH, BTL.custom_behaviors_xpath))

    def custom_behaviors(self):
        parent = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, BTL.custom_behaviors_container_xpath)))
        children = parent.find_elements(By.CLASS_NAME, 'ng-star-inserted')
        custom_behaviors = []
        for child in children:
            custom_behaviors.append(child.text)
        return custom_behaviors

    def select_all_custom_behaviors(self):
        parent = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, BTL.custom_behaviors_container_xpath)))
        children = parent.find_elements(By.CLASS_NAME, 'ng-star-inserted')
        for child in children:
            child.click()

    def the_custom_behavior(self, sequence_number):
        parent = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, BTL.custom_behaviors_container_xpath)))
        children = parent.find_elements(By.CLASS_NAME, 'ng-star-inserted')

        return Button(self.driver, None, children[sequence_number -1])
