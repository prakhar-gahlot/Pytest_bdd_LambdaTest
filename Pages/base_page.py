import string
import random
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def get_row_count(self):
        rows = self.driver.find_elements(By.TAG_NAME, "cdk-row")
        if rows is None:
            return 0
        return len(rows)

    def get_random_str(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random string of length", length, "is:", result_str)
        return result_str

    # def get_element_list(self, locator):
    #     return self.driver.find_elements(locator)
