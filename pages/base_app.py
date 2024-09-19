from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilits.words import URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = URL.SAUCEDEMO

    def find_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
            )
        self.scroll_to_element(element)
        return element

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   element)

    def click_button(self, locator):
        search_filed = self.find_element(locator, time=2)
        search_filed.click()
        return search_filed
