from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

delay = 3

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