import pytest
import time

from Lesson6.page_objects import LoginPage


@pytest.fixture(scope="function")
def login_page(driver, request):
    url = 'opencart/admin/'
    print(url)
    driver.delete_all_cookies()
    driver.get("".join([request.config.getoption("--address"), url]))
    print("site is opened")
    return LoginPage(driver)


def test_positive(driver, login_page):
    login_page.set_username("admin")
    login_page.set_password("admin")
    login_page.login()
    time.sleep(10)
    print(driver.current_url)
    assert "dashboard" in driver.current_url


@pytest.mark.parametrize("login,password", [("admin", "ddd"), ("ddd", "admin")])
def test_negative(driver, login_page, login, password):
    login_page.set_username(login)
    login_page.set_password(password)
    login_page.login()
    time.sleep(10)
    print(driver.current_url)
    alert_text = login_page.get_alert_text()
    assert "No match for Username" in alert_text


def ttt():
    pass

