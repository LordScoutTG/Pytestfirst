from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

successMessage = (By.CLASS_NAME, "alert-success")
regSettingsChangeLink = (By.CSS_SELECTOR,
                         "div > [href=\"https://litecart.info/regional_settings?redirect_url=https%3A%2F%2Flitecart.info%2F#box-regional-settings\"]")
accountButton = (By.CSS_SELECTOR, "[class=\"fa fa-user-o\"]")
currencySelector = (By.CSS_SELECTOR, "[name='currency_code']")
submitSettingsButton = (By.CSS_SELECTOR, "button[name='save']")
euroPriceSymbols = (By.CSS_SELECTOR, "[class$='price']")
duckPageTitle = (By.CSS_SELECTOR, "h1[class='title']")
duckWithOnSaleSticker = (By
                         .XPATH, "//*[@title='On Sale']/parent::div/following::div[1]/h4")
duckWithCheaperPrice = (By
                        .XPATH, "//*[@class=\"campaign-price\"]/parent::div/preceding::h4[1]")
cartButton = (By.CSS_SELECTOR, "[id='cart']")
loginLink = (By.CSS_SELECTOR, "[href=\"https://litecart.info/login\"]")
createAccountLink = (By.CSS_SELECTOR, "[class=\"account\"] [href=\"https://litecart.info/create_account\"]")
customerServiceFooterLink = (By.CSS_SELECTOR, "[class=\"list-unstyled\"] [href=\"https://litecart.info/customer-service\"]")
loadingElement = (By.CSS_SELECTOR, "[class='loader-wrapper']")
delay = 3


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def getMostPopularDuckLocator(duckName):
        return By.XPATH, "//section[@id=\"box-popular-products\"]//a[@title='%s']".format(duckName)

    # @Step("Verify successful login")
    def successMessageIsVisible(self):
        # LOG.info("Checking success message");
        return self.find(successMessage).is_displayed()

    # @Step("Clicking on regional settings")
    def regSettingsChangeLinkClick(self):
        # LOG.info("Clicking on regional settings");
        self.find(regSettingsChangeLink).click()

    # @Step("Clicking on currency selection")
    def currencySelectorClick(self):
        # LOG.info("Clicking on currency selection");
        self.find(currencySelector).click()

    # @Step("Saving currency selection")
    def submitSettingsButtonClick(self):
        # LOG.info("Saving currency selection");
        self.find(submitSettingsButton).click()

    # @Step("Searching for euro elements in goods")
    def searchEuroPriceSymbols(self):
        # LOG.info("Searching for euro elements in goods");
        return self.finds(euroPriceSymbols)

    # @Step("Checking if Duck title is visible")
    def duckTitleIsCorrect(self):
        # LOG.info("Checking if Duck title is visible");
        return self.find(duckPageTitle).getText()

    # @Step("Searching for ducks with Sale sticker")
    def searchDucksWithOnSaleSticker(self):
        # LOG.info("Searching for ducks with Sale sticker");
        return self.finds(duckWithOnSaleSticker)

    # @Step("Searching for ducks with cheaper price")
    def searchDucksWithCheaperPrice(self):
        # LOG.info("Searching for ducks with cheaper price");
        return self.finds(duckWithCheaperPrice)

    # @Step("Clicking on Most Popular Duck at Main Page")
    def clickOnMostPopularDuck(self, duckName, browser):
        # LOG.info("Clicking on Most Popular Duck at Main Page");
        WebDriverWait(browser, delay).until(EC.presence_of_element_located(HomePage.getMostPopularDuckLocator(duckName)))
        self.find(HomePage.getMostPopularDuckLocator(duckName)).click()

    # @Step("Clicking on Cart Button")
    def clickOnCartButton(self):
        # LOG.info("Clicking on Cart Button");
        self.find(cartButton).click()

    # @Step("Clicking Account Button")
    def clickOnAccountButton(self):
        # LOG.info("Clicking Account Button");
        self.find(accountButton).click()

    # @Step("Clicking Login footer link")
    def loginLinkClick(self):
        # LOG.info("Clicking Login footer link");
        self.find(loginLink).click()

    # @Step("Clicking Customer Service footer link")
    def customerServiceFooterLinkClick(self):
        # LOG.info("Clicking Customer Service footer link");
        self.find(customerServiceFooterLink).click()

    # @Step("Clicking Create Account footer link")
    def createAccountFooterLinkClick(self):
        # LOG.info("Clicking Create Account footer link");
        self.find(createAccountLink).click()

