import pytest
import time
import urllib.parse as urlparse
import os

from Lesson11_DnD.page_objects import LoginPage, CustomMenuPage

admin_url = 'admin/'
downloads_url = "admin/index.php?route=design/custommenu"


@pytest.fixture(scope="function")
def user_token(driver, request):

    driver.delete_all_cookies()
    driver.get("".join([request.config.getoption("--address"), admin_url]))
    print("site is opened")
    login_page = LoginPage(driver)
    login_page.set_username("demo")
    login_page.set_password("demo")
    login_page.login()
    time.sleep(10)
    print(driver.current_url)
    parsed = urlparse.urlparse(driver.current_url)
    print(parsed)
    user_token = urlparse.parse_qs(parsed.query)['token'][0]
    print(user_token)
    return user_token


@pytest.mark.parametrize("el1_text,el2_text", [("test 11", "test 12")])
def test_add_downloads(driver, request, user_token, el1_text, el2_text):

    url = "".join([request.config.getoption("--address"), downloads_url, "&token=", user_token])
    driver.get(url)
    time.sleep(10)

    custom_menu_page = CustomMenuPage(driver)

    old_el1_location = custom_menu_page.get_location(el1_text)
    old_el2_location = custom_menu_page.get_location(el2_text)

    custom_menu_page.switch_elements(el1_text, el2_text)

    new_el1_location = custom_menu_page.get_location(el1_text)
    new_el2_location = custom_menu_page.get_location(el2_text)

    assert old_el1_location == new_el2_location
    assert old_el2_location == new_el1_location


