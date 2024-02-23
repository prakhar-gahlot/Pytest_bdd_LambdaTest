import json
import os
import sys
from threading import local

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Tests.environment import start_local, stop_local

assertError = local()
assertError.result = False
config_file_path = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/local.json'

with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

testName = ""


# Fixtures
@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-notifications')
    options.add_argument('--deny-permission-prompts')
    options.add_argument('--test-type')
    options.add_argument('--enable-strict-powerful-feature-restrictions')
    options.add_argument('--disable-geolocation')
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
    # Make sure to add the Chrome driver to the environment variables
    driver = webdriver.Chrome(options=options)

    assertError.result = False
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    yield driver
    driver.quit()
    stop_local()


# Enter any code that has to run before scenario is called
def pytest_bdd_before_scenario(scenario):
    global testName
    testName = str(scenario.name)
    print(testName)


def pytest_bdd_after_scenario(request):
    if assertError.result:
        if CONFIG["test_type"] == "remote":
            context = request.getfixturevalue('browser')
            context.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "At '
                'least 1 assertion failed"}}')


# Once the step completes successfully, get the fixture which has the driver object and mark the test as failure
def pytest_bdd_after_step(request, step):
    print(step)
    if CONFIG["test_type"] == "remote":
        context = request.getfixturevalue('browser')
        context.execute_script(
            'browserstack_executor: {"action":"setSessionStatus", "arguments": {''"status":"passed", "reason": "All assertions passed"}}')


def pytest_bdd_step_error(request, step):
    print(step)
    assertError.result = True
    if CONFIG["test_type"] == "remote":
        context = request.getfixturevalue('browser')
        context.execute_script(
            'browserstack_executor: {"action":"setSessionStatus", "arguments": {''"status":"failed", "reason": "All assertions failed"}}')
