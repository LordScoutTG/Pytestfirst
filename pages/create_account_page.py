from selenium.webdriver.common.by import By
from pages.base_page import BasePage

createAccountTitle = (By.CSS_SELECTOR, "h1[class=\"card-title\"]")
createAccountTitleText = "Create Account"
requiredCreateAccountFields = (By.XPATH, "//*[@required]/preceding::label[1][not(@class=\"checkbox\") and not(starts-with(text(),\" Remember Me\"))]")
requiredCreateAccountFieldsText = ("First Name", "Last Name", "Country", "Email", "Desired Password", "Confirm Password", "CAPTCHA")


class CreateAccountPage(BasePage):

    # @Step("Getting Title Create Account Page")
    def getCreateAccountTitle(self):
        # LOG.info("Getting Title Create Account Page");
        return self.find(createAccountTitle).getText()

    # @Step("Searching for fields with label 'required'")
    def searchRequiredCreateAccountFields(self):
        # LOG.info("Searching for fields with label 'required'");
        return self.finds(requiredCreateAccountFields)
