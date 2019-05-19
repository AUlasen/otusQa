from selenium import webdriver
import time

from Lesson12.exceptions import TestErrorException


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver: webdriver):
        self.driver = driver


