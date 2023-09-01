from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

duckQuantitySubmitButtonText = "Add To Cart"
quantityOrder = 10
rubberDuckTitle = (By.CSS_SELECTOR, "h1[class='title']")
duckQuantityInput = (By.CSS_SELECTOR, "[type='number']")
duckQuantitySubmitButton = (By.CSS_SELECTOR, "[name=\"add_cart_product\"]")
cartQuantity = (By.CSS_SELECTOR, "[class=\"badge quantity\"]")
availableStockStatus = (By.CSS_SELECTOR, "[class='stock-available']")
sizeOptionsMenu = (By.CSS_SELECTOR, "[name='options[Size]']")
detailsDuckBodyColor = (
By.XPATH, "//table[@class=\"table table-striped table-hover\"]//td[text()[contains(.,'Body')]]/following-sibling::td");


class RubberDucksPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def getDuckLocator(self, duckName):
        return By.CSS_SELECTOR, "[alt='%s']".format(duckName)

    # @Step("Checking Rubber Ducks title")
    def rubberDuckTitleIsVisible(self):
        # LOG.info("Checking Rubber Ducks title");
        return self.find(rubberDuckTitle).isDisplayed()

    # @Step("Clicking on Duck at Duck Page")
    def clickOnDuck(self, duckName):
        # LOG.info("Clicking on Duck at Duck Page");
        self.find(getDuckLocator(duckName)).click()

    # @Step("Clicking on Duck Quantity Input")
    def clickOnQuantityInput(self):
        # LOG.info("Clicking on Duck Quantity Input");
        self.find(duckQuantityInput).click()

    # @Step("Clicking on Duck Quantity Submit Button")
    def clickOnDuckQuantitySubmit(self):
        # LOG.info("Clicking on Duck Quantity Submit Button");
        self.find(duckQuantitySubmitButton).click()

    # @Step("Setting Quantity Input")
    def getQuantityFromInput(self, browser):
        # LOG.info("Setting Quantity Input");
        return int(str(browser.execute_script("return arguments[0].value", self.find(duckQuantityInput))))

    # @Step("Set Quantity sending keys")
    def setQuantityByKeys(self):
        # LOG.info("Set Quantity sending keys");
        self.find(duckQuantityInput).clear();
        self.find(duckQuantityInput).sendKeys(str(quantityOrder))

    # @Step("Get Quantity value from Cart box")
    def getQuantityFromCart(self):
        # LOG.info("Get Quantity value from Cart box");
        return self.find(cartQuantity).getText()

    # @Step("Size Options Menu click")
    def sizeOptionsMenuClick(self):
        # LOG.info("Size Options Menu click");
        self.find(sizeOptionsMenu).click()

    # @Step("Choosing small size")
    def choosingSmallSizeDuck(self, browser):
        # LOG.info("Choosing small size");
        RubberDucksPage.sizeOptionsMenuClick(browser)
        ActionChains(browser).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)

    # @Step("Choosing medium size")
    def choosingMediumSizeDuck(self, browser):
        # LOG.info("Choosing medium size");
        RubberDucksPage.sizeOptionsMenuClick(browser)
        ActionChains(browser).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    # @Step("Choosing large size")
    def choosingLargeSizeDuck(self, browser):
        # LOG.info("Choosing large size");
        RubberDucksPage.sizeOptionsMenuClick(browser)
        ActionChains(browser).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    # @Step("Checking if Stock Status Available and choose Small Duck")
    def assertStockStatusAndChooseSmallDuck(self, browser):
        # LOG.info("Checking if Stock Status Available and choose Small Duck");
        try:
            self.find(availableStockStatus)
            RubberDucksPage.sizeOptionsMenuClick(browser)
            RubberDucksPage.choosingSmallSizeDuck(browser)
        except NoSuchElementException:
            pass

    # @Step("Checking if Stock Status Available and choose Medium Duck")
    def assertStockStatusAndChooseMediumDuck(self, browser):
        # LOG.info("Checking if Stock Status Available and choose Medium Duck");
        try:
            self.find(availableStockStatus)
            RubberDucksPage.choosingMediumSizeDuck(browser)
        except NoSuchElementException:
            pass

    # @Step("Checking if Stock Status Available and choose Large Duck")
    def assertStockStatusAndChooseLargeDuck(self, browser):
        # LOG.info("Checking if Stock Status Available and choose Large Duck");
        try:
            self.find(availableStockStatus)
            RubberDucksPage.sizeOptionsMenuClick(browser)
            RubberDucksPage.choosingLargeSizeDuck(browser)
        except NoSuchElementException:
            pass

    # @Step("Checking correct submit button text")
    def getAddToCartButtonText(self):
        # LOG.info("Checking correct submit button text");
       return self.find(duckQuantitySubmitButton).getText()

    # @Step("Getting Duck color from details")
    def getDuckColorTextFromDetails(self):
        # LOG.info("Getting Duck color from details");
        return self.find(detailsDuckBodyColor).getText()

