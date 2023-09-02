import pytest
from selenium.webdriver.common.by import By

from pages.customer_service_page import CustomerServicePage
from pages.edit_account_page import EditAccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.main_menu import MainMenu
from pages.order_history_page import OrderHistoryPage
from pages.rubber_duck_page import RubberDucksPage

correctLoginEmail = "1123@123.com"
correctLoginPassword = "adDA12341"
customerServiceText = "Customer Service"
contactUsText = "Contact Us"
orderHistoryTitleText = "Order History"
editAccountTitleText = "Account"
logoutMessage = "You are now logged out."

@pytest.fixture(scope='function', autouse=True)
def f_wrapper_function(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.attemptLogin(correctLoginEmail, correctLoginPassword, browser)

    # @Test(description = "Checking correct Customer Service link click in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")
def test_success_customer_service_link_click(browser):
    main_menu = MainMenu(browser)
    customer_service_page = CustomerServicePage(browser)
    main_menu.verticalCustomerServiceLinkClick()
    assert customer_service_page.getCustomerServiceTitle() == customerServiceText
    assert customer_service_page.getContactUsTitle() == contactUsText

    # @Test(description = "Checking correct Order History link click in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")


def test_success_order_history_link_click(browser):
    main_menu = MainMenu(browser)
    login_page = LoginPage(browser)
    order_history_page = OrderHistoryPage(browser)
    login_page.signInMenuClick()
    main_menu.verticalOrderHistoryLinkClick()
    assert order_history_page.getOrderHistoryPageTitle() == orderHistoryTitleText

    # @Test(description = "Checking correct Edit Account link click in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")


def test_success_edit_account_link_click(browser):
    login_page = LoginPage(browser)
    main_menu = MainMenu(browser)
    edit_account_page = EditAccountPage(browser)
    login_page.signInMenuClick()
    main_menu.verticalEditAccountLinkClick()
    assert edit_account_page.getEditAccountTitle() == editAccountTitleText


    # @Test(description = "Checking correct Logout link click in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")
def test_success_logout_link_click(browser):
    login_page = LoginPage(browser)
    main_menu = MainMenu(browser)
    login_page.signInMenuClick()
    main_menu.verticalLogoutLinkClick()
    assert login_page.logout_message_text() == logoutMessage

    # @Test(description="Checking Rubber Duck link in Main Menu")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Links tests")
def test_success_vertical_menu_rd_link_click(browser):
    main_menu = MainMenu(browser)
    rubber_ducks_page = RubberDucksPage(browser)
    main_menu.clickMainMenuRDLink(browser)
    assert (rubber_ducks_page.rubberDuckTitleIsVisible(), "Unsuccessful link click")


