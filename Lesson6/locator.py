from selenium.webdriver.common.by import By

class BaseLocators():
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")

class LoginPageLocators():

    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")