from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def _find(self):
        return WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(self.locator))

    def get_attribute(self, attribute):
        web_element = self.find()
        return web_element.get_attribute(attribute)

    def element_is_displayed(self):
        try:
            self.find()
        except NoSuchElementException:
            return False
        return True

    def wait_for_element_is_displayed(self, wait_time):
        i = 0
        while i < wait_time:
            try:
                self.find()
                i = wait_time
            except NoSuchElementException:
                i = i + 1
                sleep(1)

