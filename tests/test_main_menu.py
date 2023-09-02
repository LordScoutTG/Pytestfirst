import pytest


from page.customer_service_page import CustomerServicePage
from page.edit_account_page import EditAccountPage
from page.login_page import LoginPage
from page.main_menu import MainMenu
from page.order_history_page import OrderHistoryPage
from page.rubber_duck_page import RubberDucksPage

correct_login_email = "1123@123.com"
correct_login_password = "adDA12341"
customer_service_text = "Customer Service"
contact_us_text = "Contact Us"
order_history_title_text = "Order History"
edit_account_title_text = "Account"
logout_message = "You are now logged out."

@pytest.fixture(scope='function', autouse=True)
def f_wrapper_function(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.attempt_login(correct_login_email, correct_login_password, browser)

    # @Test(description = "Checking correct Customer Service link click in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")
def test_success_customer_service_link_click(browser):
    main_menu = MainMenu(browser)
    customer_service_page = CustomerServicePage(browser)
    main_menu.vertical_customer_service_link_click()
    assert customer_service_page.get_customer_service_title() == customer_service_text
    assert customer_service_page.get_contact_us_title() == contact_us_text

    # @Test(description = "Checking correct Order History link click in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")


def test_success_order_history_link_click(browser):
    main_menu = MainMenu(browser)
    login_page = LoginPage(browser)
    order_history_page = OrderHistoryPage(browser)
    login_page.sign_in_menu_click()
    main_menu.vertical_order_history_link_click()
    assert order_history_page.get_order_history_page_title() == order_history_title_text

    # @Test(description = "Checking correct Edit Account link click in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")


def test_success_edit_account_link_click(browser):
    login_page = LoginPage(browser)
    main_menu = MainMenu(browser)
    edit_account_page = EditAccountPage(browser)
    login_page.sign_in_menu_click()
    main_menu.vertical_edit_account_link_click()
    assert edit_account_page.get_edit_account_title() == edit_account_title_text


    # @Test(description = "Checking correct Logout link click in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")
def test_success_logout_link_click(browser):
    login_page = LoginPage(browser)
    main_menu = MainMenu(browser)
    login_page.sign_in_menu_click()
    main_menu.vertical_logout_link_click()
    assert login_page.logout_message_text() == logout_message

    # @Test(description="Checking Rubber Duck link in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")
def test_success_vertical_menu_rd_link_click(browser):
    main_menu = MainMenu(browser)
    rubber_ducks_page = RubberDucksPage(browser)
    main_menu.click_main_menu_rd_link(browser)
    assert (rubber_ducks_page.rubber_duck_title_is_visible(), "Unsuccessful link click")


