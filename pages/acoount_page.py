from selenium.webdriver.common.by import By
from pages.base_page import BasePage


not_logged_in_error = "You must be logged in to view the page."
alert_message = (By.CLASS_NAME, "alert-warning")
sign_in_title = (By.CSS_SELECTOR, "[id=\"box-login\"] [class=\"card-title\"]")
sign_in_title_text = "Sign In"
create_account_title = (By.CSS_SELECTOR, "[id=\"box-login-create\"] [class=\"card-title\"]")
create_account_title_text = "Create an Account"
lost_your_password_link = (By.CSS_SELECTOR, "[href=\"https://litecart.info/reset_password?email=\"]")


class AccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # @Step("Getting text from warning message")
    def get_not_logged_in_error(self):
        # LOG.info("Getting text from warning message")
        return self.find(alert_message).text

    # @Step("Getting text from Sign In title")
    def get_sign_in_title_text(self):
        # LOG.info("Getting text from Sign In title");
        return self.find(sign_in_title).text

    # @Step("Getting text from Create Account title")
    def get_create_account_title_text(self):
        # LOG.info("Getting text from Create Account title");
        return self.find(create_account_title).text

    # @Step("Clicking 'lost your password?' link")
    def lost_your_password_link_click(self):
        # LOG.info("Clicking 'lost your password?' link");
        self.find(lost_your_password_link).click()
