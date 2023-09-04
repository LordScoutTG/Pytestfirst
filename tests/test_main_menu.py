import allure
import pytest

from page.customer_service_page import CustomerServicePage
from page.edit_account_page import EditAccountPage
from page.login_page import LoginPage
from page.main_menu import MainMenu
from page.order_history_page import OrderHistoryPage
from page.rubber_duck_page import RubberDucksPage
from tests.test_login import TestLogin

@allure.epic("Regression Tests")
@allure.feature("Main Menu Tests")
class TestMainMenu:
    @pytest.fixture(scope='function', autouse=True)
    def f_wrapper_function(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.attempt_login(TestLogin.correct_login_email, TestLogin.correct_login_password, driver)

    @allure.story("Links tests")
    @allure.description("Checking correct Customer Service link click in Main Menu")
    def test_success_customer_service_link_click(self, driver):
        main_menu = MainMenu(driver)
        customer_service_page = CustomerServicePage(driver)
        main_menu.vertical_customer_service_link_click()
        assert customer_service_page.get_customer_service_title() == customer_service_page.customer_service_text
        assert customer_service_page.get_contact_us_title() == customer_service_page.contact_us_text

    @allure.story("Links tests")
    @allure.description("Checking correct Order History link click in Main Menu")
    def test_success_order_history_link_click(self, driver):
        main_menu = MainMenu(driver)
        login_page = LoginPage(driver)
        order_history_page = OrderHistoryPage(driver)
        login_page.sign_in_menu_click()
        main_menu.vertical_order_history_link_click()
        assert order_history_page.get_order_history_page_title() == order_history_page.order_history_title_text

    @allure.story("Links tests")
    @allure.description("Checking correct Edit Account link click in Main Menu")
    def test_success_edit_account_link_click(self, driver):
        login_page = LoginPage(driver)
        main_menu = MainMenu(driver)
        edit_account_page = EditAccountPage(driver)
        login_page.sign_in_menu_click()
        main_menu.vertical_edit_account_link_click()
        assert edit_account_page.get_edit_account_title() == edit_account_page.edit_account_title_text

    @allure.story("Links tests")
    @allure.description("Checking correct Logout link click in Main Menu")
    def test_success_logout_link_click(self, driver):
        login_page = LoginPage(driver)
        main_menu = MainMenu(driver)
        login_page.sign_in_menu_click()
        main_menu.vertical_logout_link_click()
        assert login_page.logout_message_text() == login_page.logout_message

    @allure.story("Links tests")
    @allure.description("Checking Rubber Duck link in Main Menu")
    def test_success_vertical_menu_rd_link_click(self, driver):
        main_menu = MainMenu(driver)
        rubber_ducks_page = RubberDucksPage(driver)
        main_menu.click_main_menu_rd_link(driver)
        assert (rubber_ducks_page.rubber_duck_title_is_visible(), "Unsuccessful link click")
