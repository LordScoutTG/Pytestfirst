from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage

delay = 3

correctLoginEmail = "1123@123.com"
correctLoginPassword = "adDA12341"


def test_button1_exist(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.sign_in_button().is_displayed()


def test_login_field_exist(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.sign_in_button().click()
    WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"email\"]")))
    assert login_page.email_input.is_displayed()

    # @Test(description="Login with correct creds")
    # @Severity(SeverityLevel.BLOCKER)
    # @Story("Login tests")


def test_success_login_test(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    login_page.open()
    # LOG.debug("Attempting login with correct creds");
    login_page.attemptLogin(correctLoginEmail, correctLoginPassword, browser)
    assert (home_page.successMessageIsVisible(), "Login was not successful")


def test_unsuccessful_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
        # LOG.debug("Attempting login with incorrect creds");
    login_page.attemptLogin("vadim.zubovich@gmail.com", "Test1234!", browser)
    assert (login_page.unSuccessMessageIsVisible(), "Unsuccessful Login")
