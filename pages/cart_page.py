from pages.base_app import BasePage

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_availbility_in_the_basket = (
            By.XPATH, "//div[@class='cart_item']"
        )
        self.locator_cart_button = (
            By.XPATH, "//a[@class='shopping_cart_link']"
        )
        self.locator_checkout_button = (By.ID, "checkout")
        self.locator_continue_button = (By.ID, "continue")
        self.locator_finish_button = (By.ID, "finish")
        self.locator_firs_name = (By.ID, "first-name")
        self.locator_last_name = (By.ID, "last-name")
        self.locator_postal_code = (By.ID, "postal-code")

    def enter_firs_name(self, word):
        search_field = self.click_button(self.locator_firs_name)
        search_field.send_keys(word)

    def enter_last_name(self, word):
        search_field = self.click_button(self.locator_last_name)
        search_field.send_keys(word)

    def enter_postal_code(self, word):
        search_field = self.click_button(self.locator_postal_code)
        search_field.send_keys(word)

    def click_finish_butron(self):
        self.click_button(self.locator_finish_button)

    def click_continue_butron(self):
        self.click_button(self.locator_continue_button)

    def click_cart_button(self):
        self.click_button(self.locator_cart_button)

    def click_checkout_button(self):
        self.click_button(self.locator_checkout_button)

    def check_exist_product_element(self):
        try:
            self.find_element(self.locator_availbility_in_the_basket)
        except NoSuchElementException:
            return False
        return True
