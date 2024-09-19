from selenium.webdriver.common.by import By

from pages.base_app import BasePage


class SelectProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_add_product_button = (
            By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"
        )

    def click_on_the_add_button(self):
        self.click_button(self.locator_add_product_button)
