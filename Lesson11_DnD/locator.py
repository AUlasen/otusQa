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
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")


class CatalogProductAddPageLocators:
    SAVE = (By.CSS_SELECTOR, "button.btn.btn-primary")
    PRODUCT_NAME = (By.CSS_SELECTOR, "input#input-name1")
    META_TAG_TITLE = (By.CSS_SELECTOR, "input#input-meta-title1")

    DATA_TAB = (By.CSS_SELECTOR, "form#form-product ul a[href = '#tab-data']")
    MODEL = (By.CSS_SELECTOR, "input#input-model")

    IMG_TAB = (By.CSS_SELECTOR, "form#form-product ul a[href = '#tab-image']")
    IMG = (By.ID, "thumb-image")
    ADD_IMG_BTN = (By.ID, "button-image")
    ADDITIONAL_IMG_ADD_BTN = (By.CSS_SELECTOR, "#images tfoot button.btn.btn-primary")
    ADDITIONAL_IMG_ROWS = (By.CSS_SELECTOR, "#images tbody tr")


class ImageManagerLocators:
    FILE_MANAGER = (By.ID, "filemanager")
    UPLOAD_BTN = (By.ID, "button-upload")
    UPLOAD_INPUT = (By.CSS_SELECTOR, "#form-upload input")
    IMGS = (By.CSS_SELECTOR, "#filemanager a.thumbnail")


class CatalogDownloadsLocators:
    ADD_BTN = (By.CSS_SELECTOR, ".page-header a.btn.btn-primary")
    DOWNLOADS_TABLE = (By.CSS_SELECTOR, "#form-download div.table-responsive table")


class CatalogDownloadsAddLocators:
    DOWNLOAD_NAME = (By.CSS_SELECTOR, "#form-download input[placeholder = 'Download Name']")
    FILE_NAME = (By.CSS_SELECTOR, "#form-download input[placeholder = 'Filename']")
    MASK = (By.CSS_SELECTOR, "#form-download input[placeholder = 'Mask']")
    UPLOAD_BTN = (By.ID, "button-upload")
    UPLOAD_INPUT = (By.CSS_SELECTOR, "#form-upload input")
    SAVE = (By.CSS_SELECTOR, "button.btn.btn-primary")


class CustomMenuLocators:
    CUSTOM_MENU_UL = (By.CSS_SELECTOR, "#custommenu-to-edit")

