import logging

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


delay = 3


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    success_message = (By.CLASS_NAME, "alert-success")
    reg_settings_change_link = (By.CSS_SELECTOR,
                                "div > [href=\"https://litecart.info/regional_settings?redirect_url=https%3A%2F%2Flitecart.info%2F#box-regional-settings\"]")
    account_button = (By.CSS_SELECTOR, "[class=\"fa fa-user-o\"]")
    currency_selector = (By.CSS_SELECTOR, "[name='currency_code']")
    submit_settings_button = (By.CSS_SELECTOR, "button[name='save']")
    euro_price_symbols = (By.CSS_SELECTOR, "[class$='price']")
    duck_page_title = (By.CSS_SELECTOR, "h1[class='title']")
    duck_with_on_sale_sticker = (By
                                 .XPATH, "//*[@title='On Sale']/parent::div/following::div[1]/h4")
    duck_with_cheaper_price = (By
                               .XPATH, "//*[@class=\"campaign-price\"]/parent::div/preceding::h4[1]")
    cart_button = (By.CSS_SELECTOR, "[id='cart']")
    login_link = (By.CSS_SELECTOR, "[href=\"https://litecart.info/login\"]")
    create_account_link = (By.CSS_SELECTOR, "[class=\"account\"] [href=\"https://litecart.info/create_account\"]")
    customer_service_footer_link = (
        By.CSS_SELECTOR, "[class=\"list-unstyled\"] [href=\"https://litecart.info/customer-service\"]")
    # loading_element = (By.CSS_SELECTOR, "[class='loader-wrapper']")

    def get_most_popular_duck_locator(self, duck_name):
        return By.XPATH, "//section[@id=\"box-popular-products\"]//a[@title='{}']".format(duck_name)

    @allure.step("Verify successful login")
    def success_message_is_visible(self):
        logging.info('Checking success message')
        return self.find(self.success_message).is_displayed()

    @allure.step("Clicking on regional settings")
    def reg_settings_change_link_click(self):
        logging.info('Clicking on regional settings')
        self.find(self.reg_settings_change_link).click()

    @allure.step("Clicking on currency selection")
    def currency_selector_click(self):
        logging.info('Clicking on currency selection')
        self.find(self.currency_selector).click()

    @allure.step("Finding currency select menu")
    def currency_selector_find(self):
        logging.info('Finding currency select menu')
        return self.find(self.currency_selector)

    @allure.step("Saving currency selection")
    def submit_settings_button_click(self):
        logging.info('Saving currency selection')
        self.find(self.submit_settings_button).click()

    @allure.step("Searching for euro elements in goods")
    def search_euro_price_symbols(self):
        logging.info('Searching for euro elements in goods')
        return self.finds(self.euro_price_symbols)

    @allure.step("Checking if Duck title is visible")
    def duck_title_is_correct(self):
        logging.info('Checking if Duck title is visible')
        return self.find(self.duck_page_title).text

    @allure.step("Searching for ducks with Sale sticker")
    def search_ducks_with_on_sale_sticker(self):
        logging.info('Searching for ducks with Sale sticker')
        return self.finds(self.duck_with_on_sale_sticker)

    @allure.step("Searching for ducks with cheaper price")
    def search_ducks_with_cheaper_price(self):
        logging.info('Searching for ducks with cheaper price')
        return self.finds(self.duck_with_cheaper_price)

    @allure.step("Clicking on Most Popular Duck at Main Page")
    def click_on_most_popular_duck(self, duck_name, driver):
        logging.info('Clicking on Most Popular Duck at Main Page')
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(self.get_most_popular_duck_locator(duck_name)))
        self.find(self.get_most_popular_duck_locator(duck_name)).click()

    @allure.step("Clicking on Cart Button")
    def click_on_cart_button(self):
        logging.info('Clicking on Cart Button')
        self.find(self.cart_button).click()

    @allure.step("Clicking Account Button")
    def click_on_account_button(self):
        logging.info('Clicking Account Button')
        self.find(self.account_button).click()

    @allure.step("Clicking Login footer link")
    def login_link_click(self):
        logging.info('Clicking Login footer link')
        self.find(self.login_link).click()

    @allure.step("Clicking Customer Service footer link")
    def customer_service_footer_link_click(self):
        logging.info('Clicking Customer Service footer link')
        self.find(self.customer_service_footer_link).click()

    @allure.step("Clicking Create Account footer link")
    def create_account_footer_link_click(self):
        logging.info('Clicking Create Account footer link')
        self.find(self.create_account_link).click()
