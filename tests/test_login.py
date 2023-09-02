from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage

delay = 3
email_input_box = (By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"email\"]")

correct_login_email = "1123@123.com"
correct_login_password = "adDA12341"


def test_button1_exist(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.sign_in_button().is_displayed()


def test_login_field_exist(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.sign_in_button().click()
    WebDriverWait(browser, delay).until(EC.element_to_be_clickable(email_input_box))
    assert login_page.email_input.is_displayed()

    # @Test(description="Login with correct creds")
    # @Severity(SeverityLevel.BLOCKER)
    # @Story("Login tests")


def test_success_login_test(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    login_page.open()
    # LOG.debug("Attempting login with correct creds");
    login_page.attempt_login(correct_login_email, correct_login_password, browser)
    assert (home_page.success_message_is_visible(), "Login was not successful")


def test_unsuccessful_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
        # LOG.debug("Attempting login with incorrect creds");
    login_page.attempt_login("vadim.zubovich@gmail.com", "Test1234!", browser)
    assert (login_page.un_success_message_is_visible(), "Unsuccessful Login")
