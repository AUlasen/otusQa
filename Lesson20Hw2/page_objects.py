from selenium.webdriver.remote.webelement import WebElement
import time

from selenium.webdriver.support.wait import WebDriverWait

from Lesson20Hw2.exceptions import TestErrorException
from Lesson20Hw2.locator import *
from Lesson20Hw2.page import BasePage
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

    def click_save(self):
        self.driver.find_element(*CatalogProductAddPageLocators.SAVE).click()

