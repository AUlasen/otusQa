import pytest
import sys

from selenium import webdriver
from selenium.webdriver import IeOptions
from selenium.webdriver import ChromeOptions

def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.56.103/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 3000, 'pageLoad': 3000, 'script': 3000}
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
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        options = ChromeOptions()
        options.add_argument("--start-fullscreen")
        options.add_argument('--headless')
        wd = webdriver.Chrome(desired_capabilities=capabilities, options=options)
        wd.fullscreen_window()
    elif browser == 'ie':
        options = IeOptions()
        options.add_argument("--start-fullscreen")
        options.add_argument('--headless')
        wd = webdriver.Ie(options=options)
    else:
        print('Unsupported browser: '.join(browser))
        sys.exit(1)
    yield wd
    wd.quit()
