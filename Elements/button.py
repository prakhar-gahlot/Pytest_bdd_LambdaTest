from Elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.driver = driver
        self.locator = locator

    def click(self):
        self._find().click()

    def get_state(self):
        return self._find().is_enabled()

    def get_text(self):
        web_element = self._find()
        return web_element.text
