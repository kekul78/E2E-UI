from pages.login_page import LoginPage
from pages.select_product_page import SelectProductPage
from pages.cart_page import CartPage
from utilits.words import UserData, URL
from time import sleep


def test_scenario(browser):
    main_page = LoginPage(browser)
    main_page.go_to_site()
    main_page.enter_username(UserData.USERNAME)
    main_page.enter_password(UserData.PASSWORD)
    main_page.click_on_the_auth_button()
    assert browser.current_url == URL.INVENTORY

    main_page = SelectProductPage(browser)
    main_page.click_on_the_add_button()

    main_page = CartPage(browser)
    main_page.click_cart_button()
    assert main_page.check_exist_product_element()
    main_page.click_checkout_button()
    assert browser.current_url == URL.CHEKOUT_STEP_ONE
    main_page.enter_firs_name(UserData.FIRST_NAME)
    main_page.enter_last_name(UserData.LAST_NAME)
    main_page.enter_postal_code(UserData.POSTAL_CODE)
    main_page.click_continue_butron()
    main_page.click_finish_butron()

    assert browser.current_url == URL.CHEKOUT_COMPLETE
    sleep(3)
