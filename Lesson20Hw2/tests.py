import pytest
import time
import urllib.parse as urlparse
import mysql.connector

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Lesson20Hw2.page_objects import LoginPage, CatalogProductPage, CatalogProductAddPage

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


def create_prod(host, db_name, user, password, prod_name):
    conn = mysql.connector.connect(database=db_name, user=user, password=password, host=host)
    cursor = conn.cursor()

    sql = "INSERT INTO oc_product(product_id) select max(product_id)+1 from oc_product"
    cursor.execute(sql)
    prod_id = cursor.lastrowid

    print("1 record inserted, ID:", prod_id)

    sql = "UPDATE oc_product set model=%s where product_id=%s"
    val = ("Model", prod_id)
    cursor.execute(sql, val)

    sql = "INSERT INTO oc_product_description(product_id,language_id,name,meta_keyword) VALUES (%s,%s,%s,%s)"
    val = (prod_id, 1, prod_name, 'tag')
    cursor.execute(sql, val)

    conn.commit()


@pytest.mark.parametrize("prod_name,host,db_name,user,password", [("dbCreateTest", '192.168.56.103','opencart','ocuser','password')])
def test_create_product(driver, request, user_token, prod_name, host, db_name, user, password):
    create_prod(host, db_name, user, password, prod_name)

    url = "".join([request.config.getoption("--address"), product_url, "&user_token=", user_token])
    driver.get(url)

    product_page = CatalogProductPage(driver)

    assert product_page.has_product_name(prod_name) is True


