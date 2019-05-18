from selenium.webdriver.remote.webelement import WebElement
import time
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.wait import WebDriverWait

from Lesson11.exceptions import TestErrorException
from Lesson11.locator import *
from Lesson11.page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def login(self):
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def get_alert_text(self):
        return self.driver.find_element(*LoginPageLocators.ERROR).get_attribute('innerHTML')


class CatalogProductPage(BasePage):

    def click_new(self):
        self.driver.find_element(*CatalogProductPageLocators.NEW).click()

    def click_del(self):
        self.driver.find_element(*CatalogProductPageLocators.DELETE).click()

    def select_product_by_name(self, prod_name):
        tr_el = self._locate_product_tr_element(prod_name)
        if tr_el is None:
            raise TestErrorException("Element with name ".join("prod_name").join(" doesnt exists"))
        td_list = tr_el.find_elements(By.TAG_NAME, "td")
        td_list[0].find_element(By.TAG_NAME, "input").click()

    # def has_product_name(self, prod_name):
    #     table: WebElement = self.driver.find_element(*CatalogProductPageLocators.PRODUCT_TABLE)
    #     tr_list = table.find_elements(By.TAG_NAME, "tr")
    #     for tr_el in tr_list:
    #         td_list = tr_el.find_elements(By.TAG_NAME, "td")
    #         cur_prod_name: str = td_list[2].get_attribute('innerText')
    #         if cur_prod_name == prod_name:
    #             return True
    #     return False

    def has_product_name(self, prod_name):
        tr = self._locate_product_tr_element(prod_name)
        if tr is not None:
            return True
        return False

    def click_edit_product_by_name(self, prod_name):
        tr_el = self._locate_product_tr_element(prod_name)
        td_list = tr_el.find_elements(By.TAG_NAME, "td")
        td_list[7].find_element(By.TAG_NAME, "a").click()

    def _locate_product_tr_element(self, prod_name) -> WebElement:
        table: WebElement = self.driver.find_element(*CatalogProductPageLocators.PRODUCT_TABLE)
        tr_list = table.find_elements(By.TAG_NAME, "tr")
        for tr_el in tr_list:
            td_list = tr_el.find_elements(By.TAG_NAME, "td")
            cur_prod_name: str = td_list[2].get_attribute('innerText')
            if cur_prod_name == prod_name:
                return tr_el

        pagination_lst: list = self.driver.find_elements(*CatalogProductPageLocators.PAGINATION)
        if pagination_lst.__len__() != 0:
            pagination: WebElement = pagination_lst[0]
            pagination_btn_list = pagination.find_elements(By.TAG_NAME, "a")
            for pag_btn in pagination_btn_list:
                if pag_btn.get_attribute('innerText') == ">":
                    pag_btn.click()
                    time.sleep(5)
                    return self._locate_product_tr_element(prod_name)

        return None

    def wait_success(self, time_to_wait):
        wait = WebDriverWait(self.driver, time_to_wait)
        wait.until(EC.element_to_be_clickable(CatalogProductPageLocators.SUCCESS_ALERT))


class CatalogProductAddPage(BasePage):
    def set_product_name(self, prod_name):
        self.driver.find_element(*CatalogProductAddPageLocators.PRODUCT_NAME).clear()
        self.driver.find_element(*CatalogProductAddPageLocators.PRODUCT_NAME).send_keys(prod_name)

    def set_meta_tag(self, meta_tag):
        self.driver.find_element(*CatalogProductAddPageLocators.META_TAG_TITLE).clear()
        self.driver.find_element(*CatalogProductAddPageLocators.META_TAG_TITLE).send_keys(meta_tag)

    def set_model(self, model):
        self.driver.find_element(*CatalogProductAddPageLocators.MODEL).clear()
        self.driver.find_element(*CatalogProductAddPageLocators.MODEL).send_keys(model)

    def click_data_tab(self):
        self.driver.find_element(*CatalogProductAddPageLocators.DATA_TAB).click()

    def click_img_tab(self):
        self.driver.find_element(*CatalogProductAddPageLocators.IMG_TAB).click()

    def start_upload_img(self):
        self.driver.find_element(*CatalogProductAddPageLocators.IMG).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(CatalogProductAddPageLocators.ADD_IMG_BTN))
        self.driver.find_element(*CatalogProductAddPageLocators.ADD_IMG_BTN).click()

    def upload_additional_img(self):
        rows: list = self.driver.find_elements(*CatalogProductAddPageLocators.ADDITIONAL_IMG_ROWS)
        row_num = rows.__len__()
        self.driver.find_element(*CatalogProductAddPageLocators.ADDITIONAL_IMG_ADD_BTN).click()

        self.driver.find_element(By.ID, "thumb-image" + str(row_num)).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(CatalogProductAddPageLocators.ADD_IMG_BTN))
        self.driver.find_element(*CatalogProductAddPageLocators.ADD_IMG_BTN).click()


    def click_save(self):
        self.driver.find_element(*CatalogProductAddPageLocators.SAVE).click()


class ImageManager(BasePage):

    def wait_existence(self, time_to_wait):
        wait = WebDriverWait(self.driver, time_to_wait)
        wait.until(EC.element_to_be_clickable(ImageManagerLocators.FILE_MANAGER))

    def upload_img(self, img_path, user_token):
        wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("$('#form-upload').remove();")
        self.driver.execute_script(" $('body').prepend('<form enctype=\"multipart/form-data\" id=\"form-upload\" ><input type=\"file\" name=\"file[]\" value=\"\" multiple=\"multiple\" /></form>');")
        self.driver.find_element(*ImageManagerLocators.UPLOAD_INPUT).send_keys(img_path)

        fun = ("$.ajax({"
            "url: 'index.php?route=common/filemanager/upload&user_token=") + user_token + ("&directory=',"
            "type: 'post',"
            "dataType: 'json',"
            "data: new FormData($('#form-upload')[0]),"
        "cache: false,"
        "contentType: false,"
        "processData: false,"
        "beforeSend: function()"
        "{"
        "$('#button-upload i').replaceWith('<i class=\"fa fa-circle-o-notch fa-spin\"></i>');"
        "$('#button-upload').prop('disabled', true);"
        "},"
        "complete: function()"
        "{"
        "$('#button-upload i').replaceWith('<i class=\"fa fa-upload\"></i>');"
        "$('#button-upload').prop('disabled', false);"
        "},"
        "success: function(json)"
        "{"
        "if (json['error'])"
        "{"
         "   alert(json['error']);"
        "}"

        "if (json['success']) {"
        "alert(json['success']);"

        "$('#button-refresh').trigger('click');"
        "}"
        "},"
        "error: function(xhr, ajaxOptions, thrownError)"
        "{"
         "   alert(thrownError + "  " + xhr.statusText + "  " + xhr.responseText);"
        "}"
        "});")

        self.driver.execute_script(fun)
        wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        #self.driver.execute_script("$('#form-upload').remove();")



    def select_img(self, img_name):
        img_lst = self.driver.find_elements(*ImageManagerLocators.IMGS)
        for img in img_lst:
            href = img.get_attribute('href')
            if href.endswith(img_name):
                img.click()
                return
        raise TestErrorException("Cant find img ".join(img_name))
