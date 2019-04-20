from selenium.webdriver.remote.webelement import WebElement

from Lesson7.locator import *
from Lesson7.page import BasePage
from selenium.webdriver.common.by import By


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
        table: WebElement = self.driver.find_element(*CatalogProductPageLocators.PRODUCT_TABLE)
        tr_list = table.find_elements(By.TAG_NAME, "tr")
        for tr_el in tr_list:
            td_list = tr_el.find_elements(By.TAG_NAME, "td")
            cur_prod_name: str = td_list[2].get_attribute('innerText')
            if cur_prod_name == prod_name:
                td_list[0].find_element(By.TAG_NAME, "input").click()
                break

    def has_product_name(self, prod_name):
        table: WebElement = self.driver.find_element(*CatalogProductPageLocators.PRODUCT_TABLE)
        tr_list = table.find_elements(By.TAG_NAME, "tr")
        for tr_el in tr_list:
            td_list = tr_el.find_elements(By.TAG_NAME, "td")
            cur_prod_name: str = td_list[2].get_attribute('innerText')
            if cur_prod_name == prod_name:
                return True
        return False


class CatalogProductAddPage(BasePage):
    def set_product_name(self, prod_name):
        self.driver.find_element(*CatalogProductAddPageLocators.PRODUCT_NAME).send_keys(prod_name)

    def set_meta_tag(self, meta_tag):
        self.driver.find_element(*CatalogProductAddPageLocators.META_TAG_TITLE).send_keys(meta_tag)

    def set_model(self, model):
        self.driver.find_element(*CatalogProductAddPageLocators.MODEL).send_keys(model)

    def click_data_tab(self):
        self.driver.find_element(*CatalogProductAddPageLocators.DATA_TAB).click()

    def click_save(self):
        self.driver.find_element(*CatalogProductAddPageLocators.SAVE).click()

