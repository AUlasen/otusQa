from selenium.webdriver.common.by import By


class BaseLocators:
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn-primary")


class LoginPageLocators:

    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
