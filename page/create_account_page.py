import logging

import allure
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    create_account_title = (By.CSS_SELECTOR, "h1[class=\"card-title\"]")
    create_account_title_text = "Create Account"
    required_create_account_fields = (
        By.XPATH,
        "//*[@required]/preceding::label[1][not(@class=\"checkbox\") and not(starts-with(text(),\" Remember Me\"))]")
    required_create_account_fields_text = (
        "First Name", "Last Name", "Country", "Email", "Desired Password", "Confirm Password", "CAPTCHA")

    @allure.step("Getting Title Create Account Page")
    def get_create_account_title(self):
        logging.info('Getting Title Create Account Page')
        return self.find(self.create_account_title).text

    @allure.step("Searching for fields with label 'required'")
    def search_required_create_account_fields(self):
        logging.info('Searching for fields with label "required"')
        return self.finds(self.required_create_account_fields)
