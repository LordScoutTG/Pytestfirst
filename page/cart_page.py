import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from page.base_page import BasePage

delay = 3  # seconds


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    empty_cart_text = "There are no items in your cart."
    remove_from_cart_button = (By.CSS_SELECTOR, "[name=\"remove_cart_item\"]")
    cart_title = (By.CSS_SELECTOR, "[class=\"cart wrapper\"] [class=\"card-title\"]")
    cart_text = (By.CSS_SELECTOR, "[class=\"text-center\"]")
    unregistered_error_message = (By.CSS_SELECTOR, "[class=\"error\"]")
    unregistered_error_no_first_name_text = "Customer Details: You must enter a first name."
    # unregistered_error_no_last_name_text = "Customer Details: You must enter a last name."
    # unregistered_error_no_address_text = "Customer Details: You must enter an address."
    # unregistered_error_no_city_text = "Customer Details: You must enter a city."
    # unregistered_error_no_email_text = "Customer Details: You must enter an email address."
    # unregistered_error_no_phone_text = "Customer Details: You must enter a phone number."
    # unregistered_error_no_post_code_text = "Customer Details: You must enter a postcode."
    # first_name_cart_input = (By.NAME, "firstname")
    # last_name_cart_input = (By.NAME, "lastname")
    # address1_cart_input = (By.NAME, "address1")
    # city_cart_input = (By.NAME, "city")
    # email_cart_input = (By.NAME, "email")
    # phone_cart_input = (By.CSS_SELECTOR, "[class=\"input-group\"] [name=\"phone\"]")
    # post_code_cart_input = (By.CSS_SELECTOR, "[class=\"form-control\"][name=\"postcode\"]")
    save_changes_button = (By.CSS_SELECTOR, "[name=\"save_customer_details\"][type='submit']")

    # agreement_check_box_shopping_form = (By.CSS_SELECTOR, "[class=\"form-check\"][name=\"terms_agreed\"]")

    @allure.step("Clicking Remove from Cart button")
    def click_remove_from_cart_button(self):
        logging.info('Clicking Remove from Cart button')
        self.find(self.remove_from_cart_button).click()

    @allure.step("Checking remove button is Visible")
    def if_remove_button_is_visible(self, driver):
        logging.debug('Waiting for Cart title appeared')
        WebDriverWait(driver, delay).until(EC.presence_of_element_located(CartPage.cart_title))
        logging.info('Checking remove button is Visible')
        self.find(self.remove_from_cart_button)

    @allure.step("Cleaning Cart")
    def cleaning_cart(self, driver):
        logging.info('Cleaning Cart')
        try:
            self.if_remove_button_is_visible(self, driver)
            self.click_remove_from_cart_button(self)
        except NoSuchElementException:
            pass

        WebDriverWait(driver, delay).until(EC.presence_of_element_located(self.cart_text))
        logging.debug('Waiting empty cart text appeared')
        assert self.find(self.cart_text).text == self.empty_cart_text

    @allure.step("Getting unregistered error message text")
    def get_unregistered_error_message_text(self):
        logging.info('Getting unregistered error message text')
        return self.find(self.unregistered_error_message).text

    @allure.step("Saving shopping cart changes")
    def saving_shopping_cart_changes(self):
        logging.info('Saving shopping cart changes')
        self.find(self.save_changes_button).click()
