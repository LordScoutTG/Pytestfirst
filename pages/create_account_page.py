from selenium.webdriver.common.by import By
from pages.base_page import BasePage

create_account_title = (By.CSS_SELECTOR, "h1[class=\"card-title\"]")
create_account_title_text = "Create Account"
required_create_account_fields = (By.XPATH, "//*[@required]/preceding::label[1][not(@class=\"checkbox\") and not(starts-with(text(),\" Remember Me\"))]")
required_create_account_fields_text = ("First Name", "Last Name", "Country", "Email", "Desired Password", "Confirm Password", "CAPTCHA")


class CreateAccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # @Step("Getting Title Create Account Page")
    def get_create_account_title(self):
        # LOG.info("Getting Title Create Account Page");
        return self.find(create_account_title).text

    # @Step("Searching for fields with label 'required'")
    def search_required_create_account_fields(self):
        # LOG.info("Searching for fields with label 'required'");
        return self.finds(required_create_account_fields)
