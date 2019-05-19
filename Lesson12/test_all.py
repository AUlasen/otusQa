import time

import pytest
import urllib.parse as urlparse

from selenium.webdriver.common.by import By

from Lesson12.Waiter import Waiter
from Lesson12.exceptions import TestErrorException
from Lesson12.page_objects import LoginPage

admin_url = 'opencart/admin/'
product_url = "opencart/admin/index.php?route=catalog/product"


@pytest.fixture(scope="function")
def user_token(driver, request):

    driver.delete_all_cookies()
    driver.get("".join([request.config.getoption("--address"), admin_url]))
    print("site is opened")
    login_page = LoginPage(driver)
    login_page.set_username("admin")
    login_page.set_password("admin")
    login_page.login()

    def has_token():
        cur_url: str = driver.current_url
        if 'user_token' in cur_url:
            return True
        return False

    Waiter.wait(has_token, 15)

    parsed = urlparse.urlparse(driver.current_url)
    print(parsed)
    user_token = urlparse.parse_qs(parsed.query)['user_token'][0]
    print(user_token)
    return user_token


def test_1(driver, request, user_token):

    url = "".join([request.config.getoption("--address"), product_url, "&user_token=", user_token])
    driver.get(url)

