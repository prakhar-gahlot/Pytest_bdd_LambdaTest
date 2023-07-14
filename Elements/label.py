from Elements.base_element import BaseElement


class Label(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.driver = driver
        self.locator = locator

    def get_text(self):
        web_element = self._find()
        return web_element.text
