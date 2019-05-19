import os

import pytest
import sys
import logging
from logging import Logger
from selenium import webdriver
from selenium.webdriver import IeOptions
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.56.103/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--timeouts", action="store", default="15000", help="Timeouts")
    parser.addoption("--logfolder", action="store", default="C:\\temp", help="Logs folder")


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
        wd.maximize_window()
    elif browser == 'ie':
        options = IeOptions()
        options.add_argument("--start-fullscreen")
        options.add_argument('--headless')
        wd = webdriver.Ie(options=options)
    else:
        print('Unsupported browser!')
        sys.exit(1)

    log_folder = request.config.getoption("--logfolder")
    logger = get_logger(log_folder, "webDriverLog")
    logged_driver = EventFiringWebDriver(wd, WdEventListener(logger))

    yield logged_driver

    if browser == 'chrome':
        browser_logger = get_logger(log_folder, "chromeLog", "%(message)s")
        for l in logged_driver.get_log("browser"):
            browser_logger.info(l)
    logged_driver.quit()


def get_logger(log_folder, log_name, log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"):
    # log_folder = request.config.getoption("--logfolder")
    # log_name = "webDriverLog"
    log_file_name = log_name + ".log"
    log_file_path = os.path.join(log_folder, log_file_name)

    logger: Logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(log_file_path, mode='w')

    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    logger.info(log_name + " logger is started.")

    return logger


class WdEventListener(AbstractEventListener):

    def __init__(self, logger: Logger):
        self.logger: Logger = logger

    def before_find(self, by, value, driver):
        self.logger.info("Find dy: " + by + "; value: " + value)

    def after_find(self, by, value, driver):
        self.logger.info("Found by: " + by + "; value: " + value)

    def on_exception(self, exception, driver):
        driver.save_screenshot('screenshots/exception.png')
        self.logger.critical(exception)

    def before_navigate_to(self, url, driver):
        self.logger.info("Navigate to: " + url)

    def after_navigate_to(self, url, driver):
        self.logger.info("Current URL: " + driver.current_url)



