from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage

emptyCartText = "There are no items in your cart."
removeFromCartButton = (By.CSS_SELECTOR, "[name=\"remove_cart_item\"]")
cartTitle = (By.CSS_SELECTOR, "[class=\"cart wrapper\"] [class=\"card-title\"]")
cartText = (By.CSS_SELECTOR,"[class=\"text-center\"]")
unregisteredErrorMessage = (By.CSS_SELECTOR,"[class=\"error\"]")
unregisteredErrorNoFirstNameText = "Customer Details: You must enter a first name."
unregisteredErrorNoLastNameText = "Customer Details: You must enter a last name."
unregisteredErrorNoAddressText = "Customer Details: You must enter an address."
unregisteredErrorNoCityText = "Customer Details: You must enter a city."
unregisteredErrorNoEmailText = "Customer Details: You must enter an email address."
unregisteredErrorNoPhoneText = "Customer Details: You must enter a phone number."
unregisteredErrorNoPostCodeText = "Customer Details: You must enter a postcode."
firstNameCartInput = (By.NAME,"firstname")
lastNameCartInput = (By.NAME,"lastname")
address1CartInput = (By.NAME,"address1")
cityCartInput = (By.NAME,"city")
emailCartInput = (By.NAME,"email")
phoneCartInput = (By.CSS_SELECTOR,"[class=\"input-group\"] [name=\"phone\"]")
postCodeCartInput = (By.CSS_SELECTOR,"[class=\"form-control\"][name=\"postcode\"]")
saveChangesButton = (By.CSS_SELECTOR,"[name=\"save_customer_details\"][type='submit']")
agreementCheckBoxShoppingForm = (By.CSS_SELECTOR,"[class=\"form-check\"][name=\"terms_agreed\"]")
delay = 3 # seconds

class CartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # @Step("Clicking Remove from Cart button")
    def clickRemoveFromCartButton(self):
        # LOG.info("Clicking Remove from Cart button");
        self.find(removeFromCartButton).click()

    # @Step("Checking remove button is Visible")
    def ifRemoveButtonIsVisible(self, browser):
        WebDriverWait(browser, delay).until(EC.presence_of_element_located(cartTitle))
        # LOG.debug("Waiting for Cart title appeared");
        # LOG.info("Checking remove button is Visible");
        self.find(removeFromCartButton)

    # @Step("Cleaning Cart")
    def cleaningCart(self, browser):
        # LOG.info("Cleaning Cart");
        try:
            CartPage.ifRemoveButtonIsVisible(self, browser)
            CartPage.clickRemoveFromCartButton(self)
        except NoSuchElementException:
            pass

        WebDriverWait(browser, delay).until(EC.presence_of_element_located(cartText))
        # LOG.debug("Waiting empty cart text appeared");
        assert self.find(cartText).text == emptyCartText

    # @Step("Getting unregistered error message text")
    def getUnregisteredErrorMessageText(self):
        # LOG.info("Getting unregistered error message text")
        return self.find(unregisteredErrorMessage).getText()

    # @Step("Saving shopping cart changes")
    def savingShoppingCartChanges(self):
        # LOG.info("Saving shopping cart changes");
        self.find(saveChangesButton).click()
