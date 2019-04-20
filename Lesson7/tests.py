import pytest
import time
import urllib.parse as urlparse

from selenium import webdriver

from Lesson7.page_objects import LoginPage, CatalogProductPage, CatalogProductAddPage

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
    time.sleep(10)
    print(driver.current_url)
    parsed = urlparse.urlparse(driver.current_url)
    print(parsed)
    user_token = urlparse.parse_qs(parsed.query)['user_token'][0]
    print(user_token)
    return user_token


@pytest.mark.skip
@pytest.mark.parametrize("prod_name", ["del_test"])
def test_delete_product(driver: webdriver, request, user_token, prod_name):
    url = "".join([request.config.getoption("--address"), product_url, "&user_token=", user_token])
    driver.get(url)
    product_page = CatalogProductPage(driver)
    product_page.select_product_by_name(prod_name)
    product_page.click_del()
    driver.switch_to.alert.accept()
    time.sleep(10)
    assert product_page.has_product_name(prod_name) is False


@pytest.mark.parametrize("prod_name,meta_tag_title,model", [("create_test", "create_test", "create_test")])
def test_create_product(driver: webdriver, request, user_token, prod_name, meta_tag_title, model):

    url = "".join([request.config.getoption("--address"), product_url, "&user_token=", user_token])
    driver.get(url)

    product_page = CatalogProductPage(driver)
    product_page.click_new()
    time.sleep(5)

    add_page = CatalogProductAddPage(driver)
    add_page.set_product_name(prod_name)
    add_page.set_meta_tag(meta_tag_title)
    add_page.click_data_tab()
    add_page.set_model(model)
    add_page.click_save()
    time.sleep(5)

    assert product_page.has_product_name(prod_name) is True
