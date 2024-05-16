from os import environ
from threading import local
import pytest
from selenium import webdriver

assertError = local()
assertError.result = False

@pytest.fixture(scope='session')
def browser(request, browser_name):
    test_name = request.node.name
    build = environ.get('BUILD', "Sample PY Build")
    tunnel_id = environ.get('TUNNEL', True)
    username = environ.get('LT_USERNAME', None)
    access_key = environ.get('LT_ACCESS_KEY', None)

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)

    def _browser(browser_name):
        driver = None
        if browser_name.lower() == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            # for key, value in browser_options.items():
            #     setattr(chrome_options, key, value)
            driver = webdriver.Remote(
                command_executor=selenium_endpoint,
                options=chrome_options,
            )
        elif browser_name.lower() == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            # for key, value in browser_options.items():
            #     setattr(firefox_options, key, value)
            driver = webdriver.Remote(
                command_executor=selenium_endpoint,
                options=firefox_options,
            )
        # Add more elif blocks for other browsers as needed

        assertError.result = False
        return driver

    browser = _browser(browser_name="firefox")
    yield browser

    if browser is not None:
        browser.quit()

@pytest.mark.parametrize('browser_name, browser_options', [
    ('chrome', {"platform": "Windows 10", "version": "latest", "name": "chrome_test", "video": True}),
    ('firefox', {"platform": "Windows 10", "version": "latest", "name": "firefox_test", "video": True})
    # Add more browsers and their options here
])
def test_example(browser, browser_name, browser_options):
    driver = browser(browser_name, browser_options)
    # Your test logic here
    driver.get("https://www.example.com")
    assert "Example Domain" in driver.title

def pytest_bdd_after_scenario(request):
    if assertError.result:
        context = request.getfixturevalue('browser')
        context.execute_script("lambda-status=failed")

def pytest_bdd_after_step(request):
    context = request.getfixturevalue('browser')
    context.execute_script("lambda-status=passed")

def pytest_bdd_step_error(request):
    assertError.result = True
    context = request.getfixturevalue('browser')
    context.execute_script("lambda-status=failed")
