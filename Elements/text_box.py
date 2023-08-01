from selenium.webdriver.common.keys import Keys
from Elements.base_element import BaseElement


class TextBox(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.driver = driver
        self.locator = locator

    def type(self, input_text, attempts=5):
        self.type_ignore_exceptions(input_text, attempts)

    def clear(self):
        self._find().clear()

    def get_text(self, expected_text='', attempts=5):
        return self.wait_for_expected_text(expected_text, attempts)

    def remove_text(self):
        self.clear()
        self.type(' ')
        self._find().send_keys(Keys.BACK_SPACE)
