import logging

import allure
from selenium.webdriver.common.by import By
from page.base_page import BasePage

customer_service_title = (By.CSS_SELECTOR, "[class=\"card-title\"]")
contact_us_title = (By.CSS_SELECTOR, "[class=\"col-md-8\"] h1")
reset_password_title = (By.CSS_SELECTOR, "[id=\"box-reset-password\"] [class=\"card-title\"]")
required_contact_us_fields = (
    By.XPATH, "//input[@required]/preceding::label[1] | //textarea[@required]/preceding::label[1]")
customer_service_text = "Customer Service"
contact_us_text = "Contact Us"
reset_password_text = "Reset Password"
required_contact_us_fields_text = ("First Name", "Last Name", "Email Address", "Subject", "Message", "CAPTCHA")


class CustomerServicePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Getting Title Customer Service Page")
    def get_customer_service_title(self):
        logging.info('Getting Title Customer Service Page')
        return self.find(customer_service_title).text

    @allure.step("Getting Title Contact Us block")
    def get_contact_us_title(self):
        logging.info('Getting Title Contact Us block')
        return self.find(contact_us_title).text

    @allure.step("Getting Title Reset Password block")
    def get_reset_password_title(self):
        logging.info('Getting Title Reset Password block')
        return self.find(reset_password_title).text

    @allure.step("Searching for fields with label 'required'")
    def search_required_contact_us_fields(self):
        logging.info('Searching for fields with label "required"')
        return self.finds(required_contact_us_fields)
