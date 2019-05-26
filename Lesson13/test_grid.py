import platform

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope="session", autouse=False)
def ff_driver(request):

    timeout = 10000

    capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
    capabilities['timeouts'] = {'implicit': timeout, 'pageLoad': timeout, 'script': timeout}
    capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
    profile = webdriver.FirefoxProfile()
    profile.set_preference('app.update.auto', False)
    profile.set_preference('app.update.enabled', False)
    profile.accept_untrusted_certs = True
    wd = WebDriver(browser_profile=profile, desired_capabilities=capabilities)
    wd.maximize_window()

    yield wd

    wd.quit()


@pytest.fixture(scope="session", autouse=False)
def ch_driver(request):
    timeout = 10000

    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    capabilities['timeouts'] = {'implicit': timeout, 'pageLoad': timeout, 'script': timeout}
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True
    wd = WebDriver(desired_capabilities=capabilities)
    wd.maximize_window()

    yield wd

    wd.quit()

def test_ff1(ff_driver):
    print("OS: " + platform.system() + platform.release())
    ff_driver.get("https://www.google.com/")

def test_ch1(ch_driver):
    print(platform.system() + platform.release())
    ch_driver.get("https://www.google.com/")




