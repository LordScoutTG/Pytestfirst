from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

categoriesMenuButton = (By.CSS_SELECTOR, "[class=\"nav-item categories dropdown\"]")
categoriesRubberDuckLink = (By.CSS_SELECTOR, "[class=\"nav-item\"] > [href=\"https://litecart.info/rubber-ducks-c-1/\"]")
verticalCustomerServiceLink = (By.CSS_SELECTOR, "[class=\"nav-item customer-service\"] > [href=\"https://litecart.info/customer-service\"]")
verticalOrderHistoryLink = (By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/order_history\"]")
verticalEditAccountLink = (By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/edit_account\"]")
verticalLogoutLink = (By.CSS_SELECTOR, "[class=\"dropdown-menu dropdown-menu-end\"] [href=\"https://litecart.info/logout\"]")
delay = 3


class MainMenu(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # @Step("Clicking on Rubber Ducks link at Main Menu")
    def clickMainMenuRDLink(self, browser):
        # LOG.info("Clicking on Rubber Ducks link at Main Menu");
        # LOG.debug("Waiting for Categories link appeared");
        WebDriverWait(browser, delay).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class=\"nav-item categories dropdown\"]")))
        self.find(categoriesMenuButton).click()
        # LOG.debug("Waiting for RD link appeared");
        WebDriverWait(browser, delay).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class=\"nav-item\"] > [href=\"https://litecart.info/rubber-ducks-c-1/\"]")))
        self.find(categoriesRubberDuckLink).click()

    # @Step("Clicking on Customer Service at Main Menu")
    def verticalCustomerServiceLinkClick(self):
        # LOG.info("Clicking on Customer Service at Main Menu");
        self.find(verticalCustomerServiceLink).click()

    # @Step("Clicking on Order History at Main Menu")
    def verticalOrderHistoryLinkClick(self):
        # LOG.info("Clicking on Customer Service at Main Menu");
        self.find(verticalOrderHistoryLink).click()

    # @Step("Clicking on Edit Account at Main Menu")
    def verticalEditAccountLinkClick(self):
        # LOG.info("Clicking on Customer Service at Main Menu");
        self.find(verticalEditAccountLink).click()

    # @Step("Clicking on Logout at Main Menu")
    def verticalLogoutLinkClick(self):
        # LOG.info("Clicking on Customer Service at Main Menu");
        self.find(verticalLogoutLink).click()

