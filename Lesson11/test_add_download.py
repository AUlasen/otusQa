import pytest
import time
import urllib.parse as urlparse
import os

from Lesson11.page_objects import LoginPage, CatalogDownloadsPage, CatalogDownloadsAddPage

admin_url = 'opencart/admin/'
downloads_url = "opencart/admin/index.php?route=catalog/download"


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


@pytest.mark.parametrize("download_name,mask,file_name", [("download1", "download1", "otus.jpg")])
def test_add_downloads(driver, request, user_token, download_name, mask, file_name):

    url = "".join([request.config.getoption("--address"), downloads_url, "&user_token=", user_token])
    driver.get(url)

    downloads_page = CatalogDownloadsPage(driver)
    downloads_page.click_add_btn()

    download_add_page = CatalogDownloadsAddPage(driver)
    download_add_page.set_download_name(download_name)
    download_add_page.set_mask(mask)

    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, file_name)
    download_add_page.upload_file(file_path, user_token)

    download_add_page.click_save()

    downloads_page = CatalogDownloadsPage(driver)
    assert downloads_page.has_download(download_name) is True

