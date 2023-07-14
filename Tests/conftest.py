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
    TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

    print("Path to the config file = %s" % (config_file_path))

    # Edit these to match your credentials
    USERNAME = os.environ.get('BROWSERSTACK_USERNAME') or sys.argv[1]
    BROWSERSTACK_ACCESS_KEY = os.environ.get('BROWSERSTACK_ACCESS_KEY') or sys.argv[2]

    if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
        raise Exception("Please provide your BrowserStack username and access key")

    desired_capabilities = CONFIG['environments'][TASK_ID]
    f = open('test.txt', 'w')
    f.write(repr(desired_capabilities))
    f.close()
    for key in CONFIG["capabilities"]:
        if key not in desired_capabilities:
            desired_capabilities[key] = CONFIG["capabilities"][key]

    if os.getenv("BROWSERSTACK_LOCAL") is not None:
        desired_capabilities["browserstack.local"] = os.getenv("BROWSERSTACK_LOCAL")
    print(os.getenv("BROWSERSTACK_BUILD_NAME"))

    if os.getenv("BROWSERSTACK_BUILD_NAME") is not None:
        print(os.getenv("BROWSERSTACK_BUILD_NAME"))
        desired_capabilities["build"] = os.getenv("BROWSERSTACK_BUILD_NAME")

    if "browserstack.local" in desired_capabilities and desired_capabilities["browserstack.local"]:
        desired_capabilities["browserstack.localIdentifier"] = USERNAME + "_" + str(TASK_ID)
        start_local()

    url = "https://%s:%s@hub.browserstack.com/wd/hub" % (
        USERNAME, BROWSERSTACK_ACCESS_KEY
    )
    print('url:' + url)
    for key in CONFIG["capabilities"]:
        print(desired_capabilities[key])
    desired_capabilities["name"] = testName

    for cap_key in desired_capabilities.keys():
        options.set_capability(cap_key, desired_capabilities[cap_key])

    if CONFIG["test_type"] == "remote":
        driver = webdriver.Remote(options=options, command_executor=url)
    else:
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
