import string
import random
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def get_row_count(self, attempts=3):
        i = 0
        while i < attempts:
            i += 1
            try:
                WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, "mat-table")))
                break
            except (TimeoutException, NoSuchElementException):
                sleep(1)

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, "mat-table")))
        sleep(3)
        rows = self.driver.find_elements(By.TAG_NAME, "mat-row")
        if rows is None:
            return 0
        return len(rows)

    def get_random_str(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random string of length", length, "is:", result_str)
        return result_str

    def refresh_page(self):
        self.driver.refresh()
        sleep(5)

    def drag_and_drop(self, x=0, y=0):
        ActionChains(self.driver).click_and_hold().move_by_offset(x, y).release().perform()
        sleep(1)
