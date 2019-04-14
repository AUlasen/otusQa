import pytest
from selenium import webdriver
import selenium
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions



class App:
    wd = None


@pytest.fixture(scope="session", autouse=True)
def session_fixture(request):
    print('\nSession was started')

    browser = request.config.getoption("--browser")
    #
    if browser == 'chrome':
        print("chrome")
        options = ChromeOptions()
        options.add_argument("--start-fullscreen")
        options.add_argument('--headless')
        App.wd = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        print("firefox")
        options = FirefoxOptions()
        options.add_argument("--start-fullscreen")
        options.add_argument('--headless')
        App.wd = webdriver.Firefox()
    else:
        print("ie")
        options = IeOptions()
        options.add_argument("--start-fullscreen")
        options.add_argument('--headless')
        App.wd = webdriver.Ie()
    #
    # #return wd

    def session_fin():
        App.wd.quit()
        print('\nSesion was finished')
    #
    request.addfinalizer(session_fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None,
                     help="Enter browser")

