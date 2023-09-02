from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

success_message = (By.CLASS_NAME, "alert-success")
reg_settings_change_link = (By.CSS_SELECTOR,
                         "div > [href=\"https://litecart.info/regional_settings?redirect_url=https%3A%2F%2Flitecart.info%2F#box-regional-settings\"]")
account_button = (By.CSS_SELECTOR, "[class=\"fa fa-user-o\"]")
currency_selector = (By.CSS_SELECTOR, "[name='currency_code']")
submit_settings_button = (By.CSS_SELECTOR, "button[name='save']")
euro_price_symbols = (By.CSS_SELECTOR, "[class$='price']")
duck_page_title = (By.CSS_SELECTOR, "h1[class='title']")
duck_with_on_sale_sticker = (By
                             .XPATH, "//*[@title='On Sale']/parent::div/following::div[1]/h4")
duck_with_cheaper_price = (By
                           .XPATH, "//*[@class=\"campaign-price\"]/parent::div/preceding::h4[1]")
cart_button = (By.CSS_SELECTOR, "[id='cart']")
login_link = (By.CSS_SELECTOR, "[href=\"https://litecart.info/login\"]")
create_account_link = (By.CSS_SELECTOR, "[class=\"account\"] [href=\"https://litecart.info/create_account\"]")
customer_service_footer_link = (By.CSS_SELECTOR, "[class=\"list-unstyled\"] [href=\"https://litecart.info/customer-service\"]")
loading_element = (By.CSS_SELECTOR, "[class='loader-wrapper']")
delay = 3


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def get_most_popular_duck_locator(self, duck_name):
        return By.XPATH, "//section[@id=\"box-popular-products\"]//a[@title='{}']".format(duck_name)

    # @Step("Verify successful login")
    def success_message_is_visible(self):
        # LOG.info("Checking success message");
        return self.find(success_message).is_displayed()


    # @Step("Clicking on regional settings")
    def reg_settings_change_link_click(self):
        # LOG.info("Clicking on regional settings");
        self.find(reg_settings_change_link).click()

    # @Step("Clicking on currency selection")
    def currency_selector_click(self):
        # LOG.info("Clicking on currency selection");
        self.find(currency_selector).click()

    # @Step("Saving currency selection")
    def submit_settings_button_click(self):
        # LOG.info("Saving currency selection");
        self.find(submit_settings_button).click()

    # @Step("Searching for euro elements in goods")
    def search_euro_price_symbols(self):
        # LOG.info("Searching for euro elements in goods");
        return self.finds(euro_price_symbols)

    # @Step("Checking if Duck title is visible")
    def duck_title_is_correct(self):
        # LOG.info("Checking if Duck title is visible");
        return self.find(duck_page_title).text

    # @Step("Searching for ducks with Sale sticker")
    def search_ducks_with_on_sale_sticker(self):
        # LOG.info("Searching for ducks with Sale sticker");
        return self.finds(duck_with_on_sale_sticker)

    # @Step("Searching for ducks with cheaper price")
    def search_ducks_with_cheaper_price(self):
        # LOG.info("Searching for ducks with cheaper price");
        return self.finds(duck_with_cheaper_price)

    # @Step("Clicking on Most Popular Duck at Main Page")
    def click_on_most_popular_duck(self, duck_name, browser):
        # LOG.info("Clicking on Most Popular Duck at Main Page");
        WebDriverWait(browser, delay).until(EC.presence_of_element_located(self.get_most_popular_duck_locator(duck_name)))
        self.find(self.get_most_popular_duck_locator(duck_name)).click()

    # @Step("Clicking on Cart Button")
    def click_on_cart_button(self):
        # LOG.info("Clicking on Cart Button");
        self.find(cart_button).click()

    # @Step("Clicking Account Button")
    def click_on_account_button(self):
        # LOG.info("Clicking Account Button");
        self.find(account_button).click()

    # @Step("Clicking Login footer link")
    def login_link_click(self):
        # LOG.info("Clicking Login footer link");
        self.find(login_link).click()

    # @Step("Clicking Customer Service footer link")
    def customer_service_footer_link_click(self):
        # LOG.info("Clicking Customer Service footer link");
        self.find(customer_service_footer_link).click()

    # @Step("Clicking Create Account footer link")
    def create_account_footer_link_click(self):
        # LOG.info("Clicking Create Account footer link");
        self.find(create_account_link).click()

