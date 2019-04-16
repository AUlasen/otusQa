from Lesson6.locator import LoginPageLocators, BaseLocators
from Lesson6.page import BasePage


class LoginPage(BasePage):

    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def login(self):
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def get_alert_text(self):
        return self.driver.find_element(*LoginPageLocators.ERROR).get_attribute('innerHTML')

