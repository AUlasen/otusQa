from selenium import webdriver


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver: webdriver):
        self.driver = driver


