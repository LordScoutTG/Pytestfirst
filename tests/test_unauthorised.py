from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from pages.acoount_page import AccountPage
from pages.cart_page import CartPage
from pages.create_account_page import CreateAccountPage
from pages.customer_service_page import CustomerServicePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.main_menu import MainMenu
from pages.rubber_duck_page import RubberDucksPage

notLoggedInError = "You must be logged in to view the page."
signInTitleText = "Sign In"
createAccountTitleText = "Create an Account"
logincreateAccountTitleText = "Create Account"
resetPasswordText = "Reset Password"
requiredContactUsFieldsText = ("First Name", "Last Name", "Email Address", "Subject", "Message", "CAPTCHA")
requiredCreateAccountFieldsText = ("First Name", "Last Name", "Country", "Email", "Desired Password", "Confirm Password", "CAPTCHA")
unregisteredErrorMessage = (By.CSS_SELECTOR,"[class=\"error\"]")
unregisteredErrorNoFirstNameText = "Customer Details: You must enter a first name."

delay = 3
# @Test(description="Checking error unlogined message at Account page")
# @Severity(SeverityLevel.NORMAL)
# @Story("UnAuthorised tests")



def test_success_warning_message_is_visible(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    account_page = AccountPage(browser)
    login_page.open()
    login_page.acceptCookiesButtonClick()
    home_page.clickOnAccountButton()
    # LOG.info("Checking correct warning unlogined message");
    assert account_page.getNotLoggedInError() == notLoggedInError


    # @Test(description = "Checking correct unauthorised sign in page Title text")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("UnAuthorised tests")
def test_success_un_authorised_sign_in_page_headers_text(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    account_page = AccountPage(browser)
    login_page.open()
    login_page.acceptCookiesButtonClick()
    home_page.loginLinkClick()
    # LOG.info("Checking correct unauthorised sign in page Title text")
    assert account_page.getSignInTitleText() == signInTitleText
    assert account_page.getCreateAccountTitleText() == createAccountTitleText


    # @Test(description = "Checking correct Reset Password page Title text")
    # @Severity(SeverityLevel.MINOR)
    # @Story("UnAuthorised tests")
def test_success_reset_password_page_title_text(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    account_page = AccountPage(browser)
    customer_service_page = CustomerServicePage(browser)
    login_page.open()
    login_page.acceptCookiesButtonClick()
    home_page.loginLinkClick()
    account_page.lostYourPasswordLinkClick()
    # LOG.info("Checking correct Reset Password page Title text");
    assert customer_service_page.getResetPasswordTitle() == resetPasswordText

    # @Test(description = "Checking correct required fields at Contact Us form")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("UnAuthorised tests")
def test_success_required_contact_us_fields(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    customer_service_page = CustomerServicePage(browser)
    login_page.open()
    login_page.acceptCookiesButtonClick()
    home_page.customerServiceFooterLinkClick()
    # LOG.info("Checking correct required fields at Contact Us form")
    for i in range(len(requiredContactUsFieldsText)):
        assert customer_service_page.searchRequiredContactUsFields()[i].text == requiredContactUsFieldsText[i]

    # @Test(description = "Checking correct Create Account page Title text")
    # @Severity(SeverityLevel.MINOR)
    # @Story("UnAuthorised tests")
def test_success_create_account_page_title_text(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    create_account_page = CreateAccountPage(browser)
    login_page.open()
    login_page.acceptCookiesButtonClick()
    home_page.createAccountFooterLinkClick()
    # LOG.info("Checking correct Create Account page Title text")
    assert create_account_page.getCreateAccountTitle() == logincreateAccountTitleText


    # @Test(description = "Checking correct required fields at Create Account form")
    # @Severity(SeverityLevel.MINOR)
    # @Story("UnAuthorised tests")
def test_success_required_create_account_fields(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    create_account_page = CreateAccountPage(browser)
    login_page.open()
    login_page.acceptCookiesButtonClick()
    home_page.createAccountFooterLinkClick()
    # LOG.info("Checking correct required fields at Create Account form");
    for i in range(len(requiredCreateAccountFieldsText)):
        assert create_account_page.searchRequiredCreateAccountFields()[i].text == requiredCreateAccountFieldsText[i]

# @Test(dataProvider = "duckDataProvider", dataProviderClass = DataProviderClass.class)
#     @Severity(SeverityLevel.NORMAL)
#     @Story("Ducks shopping tests")
#     @Flaky
def test_success_warning_message_no_first_name_shopping_form(browser):
    # LOG.debug("Checking correct warning message 'No First Name' in Shopping form");
    login_page = LoginPage(browser)
    main_menu = MainMenu(browser)
    rubber_ducks_page = RubberDucksPage(browser)
    home_page = HomePage(browser)
    cart_page = CartPage(browser)
    login_page.open()
    login_page.acceptCookiesButtonClick()
    main_menu.clickMainMenuRDLink(browser)
    rubber_ducks_page.clickOnDuck("Yellow Duck")
    rubber_ducks_page.setQuantityByKeys()
    rubber_ducks_page.assertStockStatusAndChooseLargeDuck(browser)
    rubber_ducks_page.clickOnDuckQuantitySubmit()
    WebDriverWait(browser, delay).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class=\"badge quantity\"]"), "10"))
    home_page.clickOnCartButton()
    WebDriverWait(browser, delay).until(EC.presence_of_element_located(unregisteredErrorMessage))
    WebDriverWait(browser, delay).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class=\"error\"]"), unregisteredErrorNoFirstNameText))
    assert cart_page.getUnregisteredErrorMessageText() == unregisteredErrorNoFirstNameText
    cart_page.cleaningCart(browser)






