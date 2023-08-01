from time import sleep
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def _find(self):
        return WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(self.locator))

    def _click(self):
        self._find().click()

    def _type(self, input_text):
        self._find().send_keys(input_text)

    def _get_text(self):
        return self._find().text

    def get_attribute(self, attribute):
        web_element = self._find()
        return web_element.get_attribute(attribute)

    def element_is_displayed(self):
        try:
            self._find()
        except NoSuchElementException:
            return False
        return True

    def wait_for_element_is_clickable(self, wait_time=30):
        return WebDriverWait(self.driver, wait_time).until(ec.element_to_be_clickable(self.locator))

    def wait_for_expected_text(self, expected_text='', attempts=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                if expected_text == '':
                    return self._get_text()
                if expected_text in self._get_text():
                    break
                sleep(5)
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        return self._get_text()

    def wait_for_expected_number(self, expected_number='', attempts=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                if expected_number.isdigit() and int(expected_number) == self._get_text():
                    break
                if not expected_number.isdigit() and self._get_text().isdigit():
                    break
                sleep(5)
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        return self._get_text()

    def wait_for_element_displayed(self, attempts=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                if self.element_is_displayed():
                    break
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        return self.element_is_displayed()

    def wait_for_element_with_attribute(self, attribute_name, attempts=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                self.get_attribute(attribute_name)
                break
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        return self.get_attribute(attribute_name)

    def click_element_ignore_exceptions(self, attempts=5):
        self.wait_for_element_is_clickable()
        n = 0
        while n < attempts:
            n += 1
            try:
                self._click()
                break
            except (StaleElementReferenceException, ElementClickInterceptedException):
                sleep(5)
            except TimeoutException:
                sleep(1)

        if n == attempts:
            self._click()

    def type_ignore_exceptions(self, input_text, attempts=5):
        self.wait_for_element_displayed(attempts)
        n = 0
        while n < attempts:
            n += 1
            try:
                self._type(input_text)
                break
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        if n == attempts:
            self._type(input_text)
