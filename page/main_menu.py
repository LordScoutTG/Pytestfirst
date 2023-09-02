import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

categories_menu_button = (By.CSS_SELECTOR, "[class=\"nav-item categories dropdown\"]")
categories_rubber_duck_link = (
By.CSS_SELECTOR, "[class=\"nav-item\"] > [href=\"https://litecart.info/rubber-ducks-c-1/\"]")
vertical_customer_service_link = (
By.CSS_SELECTOR, "[class=\"nav-item customer-service\"] > [href=\"https://litecart.info/customer-service\"]")
vertical_order_history_link = (
By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/order_history\"]")
vertical_edit_account_link = (
By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/edit_account\"]")
vertical_logout_link = (
By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/logout\"]")
delay = 3


class MainMenu(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Clicking on Rubber Ducks link at Main Menu")
    def click_main_menu_rd_link(self, browser):
        logging.debug('Waiting for Categories link appeared')
        WebDriverWait(browser, delay).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class=\"nav-item categories dropdown\"]")))
        logging.info('Clicking on Categories link at Main Menu')
        self.find(categories_menu_button).click()
        logging.debug('Waiting for RD link appeared')
        WebDriverWait(browser, delay).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[class=\"nav-item\"] > [href=\"https://litecart.info/rubber-ducks-c-1/\"]")))
        logging.info('Clicking on Rubber Ducks link at Main Menu')
        self.find(categories_rubber_duck_link).click()

    @allure.step("Clicking on Customer Service at Main Menu")
    def vertical_customer_service_link_click(self):
        logging.info('Clicking on Customer Service at Main Menu')
        self.find(vertical_customer_service_link).click()

    @allure.step("Clicking on Order History at Main Menu")
    def vertical_order_history_link_click(self):
        logging.info('Clicking on Customer Service at Main Menu')
        self.find(vertical_order_history_link).click()

    @allure.step("Clicking on Edit Account at Main Menu")
    def vertical_edit_account_link_click(self):
        logging.info('Clicking on Customer Service at Main Menu')
        self.find(vertical_edit_account_link).click()

    @allure.step("Clicking on Logout at Main Menu")
    def vertical_logout_link_click(self):
        logging.info('Clicking on Customer Service at Main Menu')
        self.find(vertical_logout_link).click()
