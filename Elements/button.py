from Elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, driver, locator, element=None):
        super().__init__(driver, locator)
        self.driver = driver
        self.locator = locator
        self.element = element

    def click(self, attempts=3):
        self.click_element_ignore_exceptions(attempts)

    def get_state(self):
        return self._find().is_enabled()

    def get_text(self, expected_text='', attempts=3):
        return self.wait_for_expected_text(expected_text, attempts)
