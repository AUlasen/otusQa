import pytest
import time
import urllib.parse as urlparse
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Lesson11.page_objects import LoginPage, CatalogProductPage, CatalogProductAddPage, ImageManager

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


@pytest.mark.parametrize("prod_name,meta_tag_title,model,img_name,add_img_list", [("create_test", "create_test", "create_test", "otus.jpg", ["add_img_2.jpg", "add_img_3.jpg"])])
def test_create_product(driver, request, user_token, prod_name, meta_tag_title, model, img_name, add_img_list):

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

    add_page.click_img_tab()
    add_page.start_upload_img()

    dir_path = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(dir_path, img_name)

    image_manager = ImageManager(driver)
    image_manager.wait_existence(10)
    image_manager.upload_img(img_path, user_token)
    image_manager.select_img(img_name)

    for add_img_name in add_img_list:
        img_path = os.path.join(dir_path, add_img_name)
        add_page.upload_additional_img()
        image_manager = ImageManager(driver)
        image_manager.wait_existence(10)
        image_manager.upload_img(img_path, user_token)
        image_manager.select_img(add_img_name)

    add_page.click_save()

    driver.get(url)

    assert product_page.has_product_name(prod_name) is True

