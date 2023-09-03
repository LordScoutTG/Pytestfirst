import logging

import allure
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class OrderHistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    order_history_title = (By.CSS_SELECTOR, "h1[class=\"card-title\"]")
    order_history_title_text = "Order History"

    @allure.step("Getting Title Order History Page")
    def get_order_history_page_title(self):
        logging.info("Getting Title Order History Page")
        return self.find(OrderHistoryPage.order_history_title).text
