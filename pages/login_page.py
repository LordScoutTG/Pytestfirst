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
loginButton = (By.NAME, "login")
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
        self.acceptCookiesButtonClick()
        self.sign_in_button().click()
        WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name=\"login_form\"] [name=\"email\"]")))
        # LOG.debug("Writing login email")
        self.find(emailInputBox).send_keys(email)

    def setPasswordInput(self, password):
        # LOG.debug("Writing login password");
        self.find(passwordInputBox).send_keys(password)

    def clickLoginButton(self):
        # LOG.debug("Clicking login button");
        self.find(loginButton).click()

    # @Step("Login step with email: {1}, password: {2}, for method: {method}")
    def attemptLogin(self, email, password, browser):
        # LOG.info("Attempting login");
        self.setEmailInput(email, browser)
        self.setPasswordInput(password)
        self.clickLoginButton()

    def unSuccessMessageIsVisible(self):
        # LOG.info("Checking unsuccessful message");
        return self.find(unSuccessMessage).is_displayed()

    # @Step("Clicking on Sign In menu")
    def signInMenuClick(self):
        # LOG.info("Clicking on Sign In menu");
        self.find(signInButtom).click()

    # @Step("Accepting Cookies")
    def acceptCookiesButtonClick(self):
        # LOG.info("Accepting Cookies");
        self.find(acceptCookies).click()
