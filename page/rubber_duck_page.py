import logging

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class RubberDucksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    duck_quantity_submit_button_text = "Add To Cart"
    quantity_order = 10
    rubber_duck_title = (By.CSS_SELECTOR, "h1[class='title']")
    duck_quantity_input = (By.CSS_SELECTOR, "[type='number']")
    duck_quantity_submit_button = (By.CSS_SELECTOR, "[name=\"add_cart_product\"]")
    cart_quantity = (By.CSS_SELECTOR, "[class=\"badge quantity\"]")
    available_stock_status = (By.CSS_SELECTOR, "[class='stock-available']")
    size_options_menu = (By.CSS_SELECTOR, "[name='options[Size]']")
    details_duck_body_color = (
        By.XPATH,
        "//table[@class=\"table table-striped table-hover\"]//td[text()[contains(.,'Body')]]/following-sibling::td")

    def get_duck_locator(self, duck_name):
        return (By.CSS_SELECTOR, "[alt='{}']".format(duck_name))

    @allure.step("Checking Rubber Ducks title")
    def rubber_duck_title_is_visible(self):
        logging.info("Checking Rubber Ducks title")
        return self.find(RubberDucksPage.rubber_duck_title).is_displayed()

    @allure.step("Clicking on Duck at Duck Page")
    def click_on_duck(self, duck_name):
        logging.info("Clicking on Duck at Duck Page")
        self.find(self.get_duck_locator(duck_name)).click()

    @allure.step("Clicking on Duck Quantity Input")
    def click_on_quantity_input(self):
        logging.info("Clicking on Duck Quantity Input")
        self.find(RubberDucksPage.duck_quantity_input).click()

    @allure.step("Clicking on Duck Quantity Submit Button")
    def click_on_duck_quantity_submit(self):
        logging.info("Clicking on Duck Quantity Submit Button")
        self.find(RubberDucksPage.duck_quantity_submit_button).click()

    @allure.step("Setting Quantity Input")
    def get_quantity_from_input(self, driver):
        logging.info("Setting Quantity Input")
        return int(
            str(driver.execute_script("return arguments[0].value", self.find(RubberDucksPage.duck_quantity_input))))

    @allure.step("Set Quantity sending keys")
    def set_quantity_by_keys(self):
        logging.info("Set Quantity sending keys")
        self.find(RubberDucksPage.duck_quantity_input).clear()
        self.find(RubberDucksPage.duck_quantity_input).send_keys(str(RubberDucksPage.quantity_order))

    @allure.step("Get Quantity value from Cart box")
    def get_quantity_from_cart(self):
        logging.info("Get Quantity value from Cart box")
        return self.find(RubberDucksPage.cart_quantity).text

    @allure.step("Size Options Menu click")
    def size_options_menu_click(self):
        logging.info("Size Options Menu click")
        self.find(RubberDucksPage.size_options_menu).click()

    @allure.step("Choosing small size")
    def choosing_small_size_duck(self, driver):
        logging.info("Choosing small size")
        self.size_options_menu_click()
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    @allure.step("Choosing medium size")
    def choosing_medium_size_duck(self, driver):
        logging.info("Choosing medium size")
        self.size_options_menu_click()
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    @allure.step("Choosing large size")
    def choosing_large_size_duck(self, driver):
        logging.info("Choosing large size")
        self.size_options_menu_click()
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
            Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    @allure.step("Checking if Stock Status Available and choose Small Duck")
    def assert_stock_status_and_choose_small_duck(self, driver):
        logging.info("Checking if Stock Status Available and choose Small Duck")
        try:
            self.find(RubberDucksPage.available_stock_status)
            self.size_options_menu_click()
            self.choosing_small_size_duck(driver)
        except NoSuchElementException:
            pass

    @allure.step("Checking if Stock Status Available and choose Medium Duck")
    def assert_stock_status_and_choose_medium_duck(self, driver):
        logging.info("Checking if Stock Status Available and choose Medium Duck")
        try:
            self.find(RubberDucksPage.available_stock_status)
            self.choosing_medium_size_duck(driver)
        except NoSuchElementException:
            pass

    @allure.step("Checking if Stock Status Available and choose Large Duck")
    def assert_stock_status_and_choose_large_duck(self, driver):
        logging.info("Checking if Stock Status Available and choose Large Duck")
        try:
            self.find(RubberDucksPage.available_stock_status)
            self.size_options_menu_click()
            self.choosing_large_size_duck(driver)
        except NoSuchElementException:
            pass

    @allure.step("Checking correct submit button text")
    def get_add_to_cart_button_text(self):
        logging.info("Checking correct submit button text")
        return self.find(RubberDucksPage.duck_quantity_submit_button).text

    @allure.step("Getting Duck color from details")
    def get_duck_color_text_from_details(self):
        logging.info("Getting Duck color from details")
        return self.find(RubberDucksPage.details_duck_body_color).text
