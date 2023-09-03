import logging
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.cart_page import CartPage
from page.create_account_page import CreateAccountPage
from page.customer_service_page import CustomerServicePage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.main_menu import MainMenu
from page.rubber_duck_page import RubberDucksPage
from page.acoount_page import AccountPage

delay = 3


class TestUnauthorised:
    @allure.story("UnAuthorised tests")
    @allure.description("Checking error unlogined message at Account page")
    def test_success_warning_message_is_visible(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        account_page = AccountPage(driver)
        login_page.open()
        login_page.accept_cookies_button_click()
        home_page.click_on_account_button()
        logging.info("Checking correct warning unlogined message")
        assert account_page.get_not_logged_in_error() == account_page.not_logged_in_error

    @allure.story("UnAuthorised tests")
    @allure.description("Checking correct unauthorised sign in page Title text")
    def test_success_un_authorised_sign_in_page_headers_text(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        account_page = AccountPage(driver)
        login_page.open()
        login_page.accept_cookies_button_click()
        home_page.login_link_click()
        logging.info("Checking correct unauthorised sign in page Title text")
        assert account_page.get_sign_in_title_text() == account_page.sign_in_title_text
        assert account_page.get_create_account_title_text() == account_page.create_account_title_text

    @allure.story("UnAuthorised tests")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Checking correct Reset Password page Title text")
    def test_success_reset_password_page_title_text(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        account_page = AccountPage(driver)
        customer_service_page = CustomerServicePage(driver)
        login_page.open()
        login_page.accept_cookies_button_click()
        home_page.login_link_click()
        account_page.lost_your_password_link_click()
        logging.info("Checking correct Reset Password page Title text")
        assert customer_service_page.get_reset_password_title() == customer_service_page.reset_password_text

    @allure.story("UnAuthorised tests")
    @allure.description("Checking correct required fields at Contact Us form")
    def test_success_required_contact_us_fields(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        customer_service_page = CustomerServicePage(driver)
        login_page.open()
        login_page.accept_cookies_button_click()
        home_page.customer_service_footer_link_click()
        logging.info("Checking correct required fields at Contact Us form")
        for i in range(len(customer_service_page.required_contact_us_fields_text)):
            assert customer_service_page.search_required_contact_us_fields()[i].text == \
                   customer_service_page.required_contact_us_fields_text[i]

    @allure.story("UnAuthorised tests")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Checking correct Create Account page Title text")
    def test_success_create_account_page_title_text(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        create_account_page = CreateAccountPage(driver)
        login_page.open()
        login_page.accept_cookies_button_click()
        home_page.create_account_footer_link_click()
        logging.info("Checking correct Create Account page Title text")
        assert create_account_page.get_create_account_title() == create_account_page.create_account_title_text

    @allure.story("UnAuthorised tests")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Checking correct required fields at Create Account form")
    def test_success_required_create_account_fields(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        create_account_page = CreateAccountPage(driver)
        login_page.open()
        login_page.accept_cookies_button_click()
        home_page.create_account_footer_link_click()
        logging.info("Checking correct required fields at Create Account form")
        for i in range(len(create_account_page.required_create_account_fields_text)):
            assert create_account_page.search_required_create_account_fields()[i].text == \
                   create_account_page.required_create_account_fields_text[i]

    @allure.story("Ducks shopping tests")
    #     @Flaky
    @allure.description("Checking correct warning message 'No First Name' in Shopping form")
    def test_success_warning_message_no_first_name_shopping_form(self, driver):
        logging.debug("Checking correct warning message 'No First Name' in Shopping form")
        login_page = LoginPage(driver)
        main_menu = MainMenu(driver)
        rubber_ducks_page = RubberDucksPage(driver)
        home_page = HomePage(driver)
        cart_page = CartPage(driver)
        login_page.open()
        login_page.accept_cookies_button_click()
        main_menu.click_main_menu_rd_link(driver)
        rubber_ducks_page.click_on_duck("Yellow Duck")
        rubber_ducks_page.set_quantity_by_keys()
        rubber_ducks_page.assert_stock_status_and_choose_large_duck(driver)
        rubber_ducks_page.click_on_duck_quantity_submit()
        WebDriverWait(driver, delay).until(
            EC.text_to_be_present_in_element(rubber_ducks_page.cart_quantity, "10"))
        home_page.click_on_cart_button()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located(cart_page.unregistered_error_message))
        WebDriverWait(driver, delay).until(
            EC.text_to_be_present_in_element(cart_page.unregistered_error_message,
                                             cart_page.unregistered_error_no_first_name_text))
        assert cart_page.get_unregistered_error_message_text() == cart_page.unregistered_error_no_first_name_text
        cart_page.cleaning_cart(driver)
