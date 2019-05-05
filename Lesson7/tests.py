import pytest
import time
import urllib.parse as urlparse

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    time.sleep(5)
    print(driver.current_url)
    parsed = urlparse.urlparse(driver.current_url)
    print(parsed)
    user_token = urlparse.parse_qs(parsed.query)['user_token'][0]
    print(user_token)
    return user_token


@pytest.mark.parametrize("prod_name", ["delete_test"])
def test_delete_product(driver, request, user_token, prod_name):

    url = "".join([request.config.getoption("--address"), product_url, "&user_token=", user_token])
    driver.get(url)

    product_page = CatalogProductPage(driver)
    product_page.select_product_by_name(prod_name)
    product_page.click_del()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    product_page.wait_success(10)

    assert product_page.has_product_name(prod_name) is False


@pytest.mark.parametrize("prod_name,meta_tag_title,model", [("create_test", "create_test", "create_test")])
def test_create_product(driver, request, user_token, prod_name, meta_tag_title, model):

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

    driver.get(url)

    assert product_page.has_product_name(prod_name) is True


@pytest.mark.parametrize("prod_name,new_prod_name", [("edit_test_before", "edit_test_after")])
def test_edit_product(driver, request, user_token, prod_name, new_prod_name):

    url = "".join([request.config.getoption("--address"), product_url, "&user_token=", user_token])
    driver.get(url)

    product_page = CatalogProductPage(driver)
    product_page.select_product_by_name(prod_name)
    product_page.click_edit_product_by_name(prod_name)

    add_page = CatalogProductAddPage(driver)
    add_page.set_product_name(new_prod_name)
    add_page.click_save()

    product_page.wait_success(10)

    assert product_page.has_product_name(new_prod_name) is True


