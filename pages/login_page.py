from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

signInButtom = (By.CSS_SELECTOR, "[class=\"nav-item account dropdown\"]>[data-toggle=\"dropdown\"]")
emailInputBox = (By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"email\"]")
unSuccessMessage = (By.CLASS_NAME, "alert-danger")
acceptCookies = (By.CSS_SELECTOR, "[name=\"accept_cookies\"]")
logoutMessage = "You are now logged out."
passwordInputBox = (By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"password\"]")
delay = 3


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://litecart.info/')

    def sign_in_button(self):
        return self.find(signInButtom)

    @property
    def email_input(self):
        return self.find(emailInputBox)

    def setEmailInput(self, email, browser):
        LoginPage.acceptCookiesButtonClick(browser)
        LoginPage.signInMenuClick(browser)
        WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"email\"]")))
        # LOG.debug("Writing login email")
        self.find(emailInputBox).sendKeys(email)

    def setPasswordInput(self, password):
        # LOG.debug("Writing login password");
        self.find(passwordInputBox).sendKeys(password)

    def clickLoginButton(self):
        # LOG.debug("Clicking login button");
        self.find(getLocator("LoginPage.loginButton")).click()

    # @Step("Login step with email: {1}, password: {2}, for method: {method}")
    def attemptLogin(self, email, password):
        # LOG.info("Attempting login");
        LoginPage.setEmailInput(email)
        LoginPage.setPasswordInput(password)
        LoginPage.clickLoginButton(browser)

    def unSuccessMessageIsVisible(self):
        # LOG.info("Checking unsuccessful message");
        return self.find(unSuccessMessage).isDisplayed()

    # @Step("Clicking on Sign In menu")
    def signInMenuClick(self):
        # LOG.info("Clicking on Sign In menu");
        self.find(signInButtom).click()

    # @Step("Accepting Cookies")
    def acceptCookiesButtonClick(self):
        # LOG.info("Accepting Cookies");
        self.find(acceptCookies).click()
