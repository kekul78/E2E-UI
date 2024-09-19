from pages.login_page import LoginPage
from pages.select_product_page import SelectProductPage
from utilits.words import UserData
# from time import sleep


def test_scenario(browser):
    main_page = LoginPage(browser)
    main_page.go_to_site()
    main_page.enter_username(UserData.USERNAME)
    main_page.enter_password(UserData.PASSWORD)
    main_page.click_on_the_auth_button()
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    main_page = SelectProductPage(browser)
    main_page.click_on_the_add_button()
    assert main_page.check_exist_product_element()
