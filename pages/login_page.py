from selenium.webdriver.common.by import By

from pages.base_app import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_login_username = (By.ID, "user-name")
        self.locator_login_password = (By.ID, "password")
        self.locator_login_button = (By.ID, "login-button")

    def click_on_the_auth_button(self):
        self.click_button(self.locator_login_button)

    def enter_username(self, word):
        search_field = self.click_button(self.locator_login_username)
        search_field.send_keys(word)

    def enter_password(self, word):
        search_field = self.click_button(self.locator_login_password)
        search_field.send_keys(word)
