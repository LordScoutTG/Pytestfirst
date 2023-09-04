import allure
from selenium.webdriver.common.by import By
from page.base_page import BasePage
import logging


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    not_logged_in_error = "You must be logged in to view the page."
    alert_message = (By.CLASS_NAME, "alert-warning")
    sign_in_title = (By.CSS_SELECTOR, "[id=\"box-login\"] [class=\"card-title\"]")
    sign_in_title_text = "Sign In"
    create_account_title = (By.CSS_SELECTOR, "[id=\"box-login-create\"] [class=\"card-title\"]")
    create_account_title_text = "Create an Account"
    lost_your_password_link = (By.CSS_SELECTOR, "[href=\"https://litecart.info/reset_password?email=\"]")

    @allure.step("Getting text from warning message")
    def get_not_logged_in_error(self):
        logging.info('Getting text from warning message')
        return self.find(self.alert_message).text

    @allure.step("Getting text from Sign In title")
    def get_sign_in_title_text(self):
        logging.info('Getting text from Sign In title')
        return self.find(self.sign_in_title).text

    @allure.step("Getting text from Create Account title")
    def get_create_account_title_text(self):
        logging.info('Getting text from Create Account title')
        return self.find(self.create_account_title).text

    @allure.step("Clicking 'lost your password?' link")
    def lost_your_password_link_click(self):
        logging.info('Clicking "lost your password?" link')
        self.find(self.lost_your_password_link).click()
