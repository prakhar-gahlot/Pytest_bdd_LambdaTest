from Elements.button import Button
from Elements.text_box import TextBox
from Elements.label import Label
from Pages.Arc.comments_tab_locator import CommentsTabLocator as CTL
from Pages.Arc.event_review_page import EventReviewPage
from selenium.webdriver.common.by import By


class CommentsTab(EventReviewPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Complete & Next button
    def complete_next(self):
        return Button(self.driver, (By.XPATH, CTL.complete_next_xpath))

    # comments
    def behaviors(self):
        behaviors = self.driver.find_elements(By.CLASS_NAME, "cdk-column-behavior")
        behavior_list = []
        for behavior in behaviors:
            behavior_list.append(behavior.text)
        return behavior_list

    def behavior_comments(self):
        comments = self.driver.find_elements(By.CLASS_NAME, "cdk-column-comment")
        comment_list = []
        for comment in comments:
            comment_list.append(comment.text)
        return comment_list
