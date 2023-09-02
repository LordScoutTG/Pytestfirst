import logging

import allure
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sign_in_buttom = (By.CSS_SELECTOR, "[class=\"nav-item account dropdown\"]>[data-toggle=\"dropdown\"]")
email_input_box = (By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"email\"]")
un_success_message = (By.CLASS_NAME, "alert-danger")
accept_cookies = (By.CSS_SELECTOR, "[name=\"accept_cookies\"]")
logout_message = "You are now logged out."
password_input_box = (By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"password\"]")
login_button = (By.NAME, "login")
success_message = (By.CLASS_NAME, "alert-success")
delay = 3


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://litecart.info/')

    def sign_in_button(self):
        return self.find(sign_in_buttom)

    @property
    def email_input(self):
        return self.find(email_input_box)

    def set_email_input(self, email, browser):
        self.accept_cookies_button_click()
        self.sign_in_button().click()
        WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"email\"]")))
        logging.debug('Writing login email')
        self.find(email_input_box).send_keys(email)

    def set_password_input(self, password):
        logging.debug('Writing login password')
        self.find(password_input_box).send_keys(password)

    def click_login_button(self):
        logging.debug('Clicking login button')
        self.find(login_button).click()

    @allure.step("Login step with email: {1}, password: {2}, for method: {method}")
    def attempt_login(self, email, password, browser):
        logging.info('Attempting login')
        self.set_email_input(email, browser)
        self.set_password_input(password)
        self.click_login_button()

    def un_success_message_is_visible(self):
        logging.info('Checking unsuccessful message')
        return self.find(un_success_message).is_displayed()


    def logout_message_text(self):
        return self.find(success_message).text

    @allure.step("Clicking on Sign In menu")
    def sign_in_menu_click(self):
        logging.info('Clicking on Sign In menu')
        self.find(sign_in_buttom).click()

    @allure.step("Accepting Cookies")
    def accept_cookies_button_click(self):
        logging.info('Accepting Cookies')
        self.find(accept_cookies).click()
