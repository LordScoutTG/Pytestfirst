import logging

from selenium.webdriver.common.by import By
from page.base_page import BasePage

order_history_title = (By.CSS_SELECTOR, "h1[class=\"card-title\"]")
order_history_title_text = "Order History"


class OrderHistoryPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # @Step("Getting Title Order History Page")
    def get_order_history_page_title(self):
        logging.info("Getting Title Order History Page")
        return self.find(order_history_title).text

    