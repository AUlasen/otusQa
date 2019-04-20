from selenium.webdriver.common.by import By


class BaseLocators:
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn-primary")


class LoginPageLocators:

    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")


class CatalogProductPageLocators:
    NEW = (By.CSS_SELECTOR, "a.btn.btn-primary")
    COPY = (By.CSS_SELECTOR, "button.btn.btn-default")
    DELETE = (By.CSS_SELECTOR, "button.btn.btn-danger")
    PRODUCT_TABLE = (By.CSS_SELECTOR, "#form-product table")
    PAGINATION = (By.CSS_SELECTOR, "ul.pagination")


class CatalogProductAddPageLocators:
    SAVE = (By.CSS_SELECTOR, "button.btn.btn-primary")
    PRODUCT_NAME = (By.CSS_SELECTOR, "input#input-name1")
    META_TAG_TITLE = (By.CSS_SELECTOR, "input#input-meta-title1")
    DATA_TAB = (By.CSS_SELECTOR, "form#form-product ul a[href = '#tab-data']")
    MODEL = (By.CSS_SELECTOR, "input#input-model")

