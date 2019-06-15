import pytest
import sys

from selenium import webdriver
from selenium.webdriver import IeOptions


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://demo23.opencart.pro/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--timeouts", action="store", default="10000", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    try:
        timeout_str = request.config.getoption("--timeouts")
        timeout = int(timeout_str)
    except ValueError:
        print("Bad --timeouts value: ".join(timeout_str))
        timeout = 10000

    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': timeout, 'pageLoad': timeout, 'script': timeout}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = webdriver.Firefox(firefox_profile=profile, capabilities=capabilities)
        wd.maximize_window()
    elif browser == 'chrome':
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['timeouts'] = {'implicit': timeout, 'pageLoad': timeout, 'script': timeout}
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        wd = webdriver.Chrome(desired_capabilities=capabilities)
        wd.fullscreen_window()
    elif browser == 'ie':
        options = IeOptions()
        options.add_argument("--start-fullscreen")
        options.add_argument('--headless')
        wd = webdriver.Ie(options=options)
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()
