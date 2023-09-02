from selenium.webdriver.common.by import By
from pages.base_page import BasePage


notLoggedInError = "You must be logged in to view the page."
alertMessage = (By.CLASS_NAME, "alert-warning")
signInTitle = (By.CSS_SELECTOR, "[id=\"box-login\"] [class=\"card-title\"]")
signInTitleText = "Sign In"
createAccountTitle = (By.CSS_SELECTOR, "[id=\"box-login-create\"] [class=\"card-title\"]")
createAccountTitleText = "Create an Account"
lostYourPasswordLink = (By.CSS_SELECTOR, "[href=\"https://litecart.info/reset_password?email=\"]")


class AccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # @Step("Getting text from warning message")
    def getNotLoggedInError(self):
        # LOG.info("Getting text from warning message")
        return self.find(alertMessage).text

    # @Step("Getting text from Sign In title")
    def getSignInTitleText(self):
        # LOG.info("Getting text from Sign In title");
        return self.find(signInTitle).text

    # @Step("Getting text from Create Account title")
    def getCreateAccountTitleText(self):
        # LOG.info("Getting text from Create Account title");
        return self.find(createAccountTitle).text

    # @Step("Clicking 'lost your password?' link")
    def lostYourPasswordLinkClick(self):
        # LOG.info("Clicking 'lost your password?' link");
        self.find(lostYourPasswordLink).click()
