from selenium.webdriver.common.by import By
from pages.base_page import BasePage

customerServiceTitle = (By.CSS_SELECTOR, "[class=\"card-title\"]")
contactUsTitle = (By.CSS_SELECTOR, "[class=\"col-md-8\"] h1")
resetPasswordTitle = (By.CSS_SELECTOR, "[id=\"box-reset-password\"] [class=\"card-title\"]")
requiredContactUsFields = (
By.XPATH, "//input[@required]/preceding::label[1] | //textarea[@required]/preceding::label[1]")
customerServiceText = "Customer Service"
contactUsText = "Contact Us"
resetPasswordText = "Reset Password"
requiredContactUsFieldsText = ("First Name", "Last Name", "Email Address", "Subject", "Message", "CAPTCHA")


class CustomerServicePage(BasePage):

    # @Step("Getting Title Customer Service Page")
    def getCustomerServiceTitle(self):
        # LOG.info("Getting Title Customer Service Page");
        return self.find(customerServiceTitle).getText()

    # @Step("Getting Title Contact Us block")
    def getContactUsTitle(self):
        # LOG.info("Getting Title Contact Us block");
        return self.find(contactUsTitle).getText()

    # @Step("Getting Title Reset Password block")
    def getResetPasswordTitle(self):
        # LOG.info("Getting Title Reset Password block");
        return self.find(resetPasswordTitle).getText()

    # @Step("Searching for fields with label 'required'")
    def searchRequiredContactUsFields(self):
        # LOG.info("Searching for fields with label 'required'");
        return self.finds(requiredContactUsFields)
