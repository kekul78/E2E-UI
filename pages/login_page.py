from pages.base_app import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_login_username = (By.ID, "user-name")
        self.locator_login_password = (By.ID, "password")
        self.locator_login_button = (By.ID, "login-button")

    def click_on_the_auth_button(self):
        search_filed = self.find_element(
            self.locator_login_button, time=2
        )
        search_filed.click()

    def enter_username(self, word):
        search_field = self.find_element(
            self.locator_login_username
        )
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_password(self, word):
        search_field = self.find_element(
            self.locator_login_password
        )
        search_field.click()
        search_field.send_keys(word)
        return search_field
