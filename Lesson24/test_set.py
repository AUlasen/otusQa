from selenium import webdriver
from selenium.webdriver import ChromeOptions



def test_1():
    assert True


def test_2():
    options = ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_argument('--headless')

    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True
    wd = webdriver.Chrome(desired_capabilities=capabilities, options=options)
    wd.get("https://ya.ru/")



def test_3():
    assert True


def test_4():
    assert True


def test_5():
    assert True

