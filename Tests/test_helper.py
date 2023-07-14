import string
from random import random
from enum import Enum
from datetime import datetime, timedelta
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class TestHelper:
    def __init__(self):
        self.driver = None

    def get_random_str(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random string of length", length, "is:", result_str)

        return result_str

    def check_file_exist(self, file_name):
        file_exist_script = 'browserstack_executor: {"action": "fileExists", "arguments": ' \
                            '{"fileName": "' + file_name + '"}}'

        return self.driver.execute_script(file_exist_script)
