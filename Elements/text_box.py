from selenium.webdriver import Keys
from Elements.base_element import BaseElement


class TextBox(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.driver = driver
        self.locator = locator

    def type(self, input_text):
        self._find().send_keys(input_text)

    def clear(self):
        self._find().clear()

    def get_text(self):
        return self._find().text

    def remove_text(self):
        self.clear()
        self.type(' ')
        self._find().send_keys(Keys.BACK_SPACE)
