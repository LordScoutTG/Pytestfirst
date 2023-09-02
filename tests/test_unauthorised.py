import logging

from selenium.webdriver.common.by import By
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

not_logged_in_error = "You must be logged in to view the page."
sign_in_title_text = "Sign In"
create_account_title_text = "Create an Account"
login_create_account_title_text = "Create Account"
reset_password_text = "Reset Password"
required_contact_us_fields_text = ("First Name", "Last Name", "Email Address", "Subject", "Message", "CAPTCHA")
required_create_account_fields_text = ("First Name", "Last Name", "Country", "Email", "Desired Password", "Confirm Password", "CAPTCHA")
unregistered_error_message = (By.CSS_SELECTOR, "[class=\"error\"]")
unregistered_error_no_first_name_text = "Customer Details: You must enter a first name."

delay = 3
# @Test(description="Checking error unlogined message at Account page")
# @Severity(SeverityLevel.NORMAL)
# @Story("UnAuthorised tests")



def test_success_warning_message_is_visible(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    account_page = AccountPage(browser)
    login_page.open()
    login_page.accept_cookies_button_click()
    home_page.click_on_account_button()
    logging.info("Checking correct warning unlogined message")
    assert account_page.get_not_logged_in_error() == not_logged_in_error


    # @Test(description = "Checking correct unauthorised sign in page Title text")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("UnAuthorised tests")
def test_success_un_authorised_sign_in_page_headers_text(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    account_page = AccountPage(browser)
    login_page.open()
    login_page.accept_cookies_button_click()
    home_page.login_link_click()
    logging.info("Checking correct unauthorised sign in page Title text")
    assert account_page.get_sign_in_title_text() == sign_in_title_text
    assert account_page.get_create_account_title_text() == create_account_title_text


    # @Test(description = "Checking correct Reset Password page Title text")
    # @Severity(SeverityLevel.MINOR)
    # @Story("UnAuthorised tests")
def test_success_reset_password_page_title_text(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    account_page = AccountPage(browser)
    customer_service_page = CustomerServicePage(browser)
    login_page.open()
    login_page.accept_cookies_button_click()
    home_page.login_link_click()
    account_page.lost_your_password_link_click()
    logging.info("Checking correct Reset Password page Title text")
    assert customer_service_page.get_reset_password_title() == reset_password_text

    # @Test(description = "Checking correct required fields at Contact Us form")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("UnAuthorised tests")
def test_success_required_contact_us_fields(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    customer_service_page = CustomerServicePage(browser)
    login_page.open()
    login_page.accept_cookies_button_click()
    home_page.customer_service_footer_link_click()
    logging.info("Checking correct required fields at Contact Us form")
    for i in range(len(required_contact_us_fields_text)):
        assert customer_service_page.search_required_contact_us_fields()[i].text == required_contact_us_fields_text[i]

    # @Test(description = "Checking correct Create Account page Title text")
    # @Severity(SeverityLevel.MINOR)
    # @Story("UnAuthorised tests")
def test_success_create_account_page_title_text(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    create_account_page = CreateAccountPage(browser)
    login_page.open()
    login_page.accept_cookies_button_click()
    home_page.create_account_footer_link_click()
    logging.info("Checking correct Create Account page Title text")
    assert create_account_page.get_create_account_title() == login_create_account_title_text


    # @Test(description = "Checking correct required fields at Create Account form")
    # @Severity(SeverityLevel.MINOR)
    # @Story("UnAuthorised tests")
def test_success_required_create_account_fields(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    create_account_page = CreateAccountPage(browser)
    login_page.open()
    login_page.accept_cookies_button_click()
    home_page.create_account_footer_link_click()
    logging.info("Checking correct required fields at Create Account form")
    for i in range(len(required_create_account_fields_text)):
        assert create_account_page.search_required_create_account_fields()[i].text == required_create_account_fields_text[i]

#
#     @Severity(SeverityLevel.NORMAL)
#     @Story("Ducks shopping tests")
#     @Flaky
def test_success_warning_message_no_first_name_shopping_form(browser):
    logging.debug("Checking correct warning message 'No First Name' in Shopping form")
    login_page = LoginPage(browser)
    main_menu = MainMenu(browser)
    rubber_ducks_page = RubberDucksPage(browser)
    home_page = HomePage(browser)
    cart_page = CartPage(browser)
    login_page.open()
    login_page.accept_cookies_button_click()
    main_menu.click_main_menu_rd_link(browser)
    rubber_ducks_page.click_on_duck("Yellow Duck")
    rubber_ducks_page.set_quantity_by_keys()
    rubber_ducks_page.assert_stock_status_and_choose_large_duck(browser)
    rubber_ducks_page.click_on_duck_quantity_submit()
    WebDriverWait(browser, delay).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class=\"badge quantity\"]"), "10"))
    home_page.click_on_cart_button()
    WebDriverWait(browser, delay).until(EC.presence_of_element_located(unregistered_error_message))
    WebDriverWait(browser, delay).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class=\"error\"]"), unregistered_error_no_first_name_text))
    assert cart_page.get_unregistered_error_message_text() == unregistered_error_no_first_name_text
    cart_page.cleaning_cart(browser)






