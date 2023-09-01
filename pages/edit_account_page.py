from selenium.webdriver.common.by import By
from pages.base_page import BasePage

editAccountTitle = (By.CSS_SELECTOR, "h2[class=\"card-title\"]")
editAccountTitleText = "Account"


class EditAccountPage(BasePage):

    # @Step("Getting Title Edit Account Page")
    def getEditAccountTitle(self):
        # LOG.info("Getting Title Edit Account Page");
        return self.find(editAccountTitle).getText()
