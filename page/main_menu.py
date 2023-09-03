import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

delay = 3


class MainMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    categories_menu_button = (By.CSS_SELECTOR, "[class=\"nav-item categories dropdown\"]")
    categories_rubber_duck_link = (
        By.CSS_SELECTOR, "[class=\"nav-item\"] > [href=\"https://litecart.info/rubber-ducks-c-1/\"]")
    main_menu_customer_service_link = (
        By.CSS_SELECTOR, "[class=\"nav-item customer-service\"] > [href=\"https://litecart.info/customer-service\"]")
    main_menu_order_history_link = (
        By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/order_history\"]")
    main_menu_edit_account_link = (
        By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/edit_account\"]")
    main_menu_logout_link = (
        By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/logout\"]")

    @allure.step("Clicking on Rubber Ducks link at Main Menu")
    def click_main_menu_rd_link(self, driver):
        logging.debug('Waiting for Categories link appeared')
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainMenu.categories_menu_button))
        logging.info('Clicking on Categories link at Main Menu')
        self.find(MainMenu.categories_menu_button).click()
        logging.debug('Waiting for RD link appeared')
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainMenu.categories_rubber_duck_link))
        logging.info('Clicking on Rubber Ducks link at Main Menu')
        self.find(MainMenu.categories_rubber_duck_link).click()

    @allure.step("Clicking on Customer Service at Main Menu")
    def vertical_customer_service_link_click(self):
        logging.info('Clicking on Customer Service at Main Menu')
        self.find(MainMenu.main_menu_customer_service_link).click()

    @allure.step("Clicking on Order History at Main Menu")
    def vertical_order_history_link_click(self):
        logging.info('Clicking on Customer Service at Main Menu')
        self.find(MainMenu.main_menu_order_history_link).click()

    @allure.step("Clicking on Edit Account at Main Menu")
    def vertical_edit_account_link_click(self):
        logging.info('Clicking on Customer Service at Main Menu')
        self.find(MainMenu.main_menu_edit_account_link).click()

    @allure.step("Clicking on Logout at Main Menu")
    def vertical_logout_link_click(self):
        logging.info('Clicking on Customer Service at Main Menu')
        self.find(MainMenu.main_menu_logout_link).click()
