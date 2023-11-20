from Elements.base_element import BaseElement


class Label(BaseElement):
    def __init__(self, driver, locator, element=None):
        super().__init__(driver, locator)
        self.driver = driver
        self.locator = locator
        self.element = element

    def get_text(self, expected_text='', attempts=5):
        return self.wait_for_expected_text(expected_text, attempts)

    def get_number(self, expected_number='', attempts=5):
        return self.wait_for_expected_text(expected_number, attempts)
