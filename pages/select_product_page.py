from pages.base_app import BasePage

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SelectProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_add_product_button = (
            By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"
        )
        self.locator_availbility_in_the_basket = (
            By.XPATH, "//span[@class='shopping_cart_badge']"
        )

    def click_on_the_add_button(self):
        search_filed = self.find_element(
            self.locator_add_product_button, time=2
        )
        search_filed.click()

    def check_exist_product_element(self):
        try:
            self.find_element(self.locator_availbility_in_the_basket)
        except NoSuchElementException:
            return False
        return True
