from selenium.webdriver.common.by import By
from pages.base_page import BasePage

orderHistoryTitle = (By.CSS_SELECTOR, "h1[class=\"card-title\"]")
orderHistoryTitleText = "Order History"


class OrderHistoryPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # @Step("Getting Title Order History Page")
    def getOrderHistoryPageTitle(self):
        # LOG.info("Getting Title Order History Page");
        return self.find(orderHistoryTitle).text

    