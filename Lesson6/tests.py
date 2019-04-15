import pytest
import time

from Lesson6.page_objects import LoginPage


@pytest.fixture(scope="function")
def login_page(driver, request):
    url = 'opencart/admin/'
    driver.delete_all_cookies()
    driver.get("".join([request.config.getoption("--address"), url]))
    return LoginPage(driver)


class LoginPageTests:

    def test_positive(self, driver, login_page):
        login_page.set_username("admin")
        login_page.set_password("admin")
        login_page.login()
        time.sleep(10)
        print(driver.current_url)
        assert "dashboard" in driver.current_url