from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

duck_quantity_submit_button_text = "Add To Cart"
quantity_order = 10
rubber_duck_title = (By.CSS_SELECTOR, "h1[class='title']")
duck_quantity_input = (By.CSS_SELECTOR, "[type='number']")
duck_quantity_submit_button = (By.CSS_SELECTOR, "[name=\"add_cart_product\"]")
cart_quantity = (By.CSS_SELECTOR, "[class=\"badge quantity\"]")
available_stock_status = (By.CSS_SELECTOR, "[class='stock-available']")
size_options_menu = (By.CSS_SELECTOR, "[name='options[Size]']")
details_duck_body_color = (By.XPATH, "//table[@class=\"table table-striped table-hover\"]//td[text()[contains(.,'Body')]]/following-sibling::td")


class RubberDucksPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def get_duck_locator(self, duckName):
        return (By.CSS_SELECTOR, "[alt='{}']".format(duckName))

    # @Step("Checking Rubber Ducks title")
    def rubber_duck_title_is_visible(self):
        # LOG.info("Checking Rubber Ducks title");
        return self.find(rubber_duck_title).is_displayed()

    # @Step("Clicking on Duck at Duck Page")
    def click_on_duck(self, duckName):
        # LOG.info("Clicking on Duck at Duck Page");
        self.find(self.get_duck_locator(duckName)).click()

    # @Step("Clicking on Duck Quantity Input")
    def click_on_quantity_input(self):
        # LOG.info("Clicking on Duck Quantity Input");
        self.find(duck_quantity_input).click()

    # @Step("Clicking on Duck Quantity Submit Button")
    def click_on_duck_quantity_submit(self):
        # LOG.info("Clicking on Duck Quantity Submit Button");
        self.find(duck_quantity_submit_button).click()

    # @Step("Setting Quantity Input")
    def get_quantity_from_input(self, browser):
        # LOG.info("Setting Quantity Input");
        return int(str(browser.execute_script("return arguments[0].value", self.find(duck_quantity_input))))

    # @Step("Set Quantity sending keys")
    def set_quantity_by_keys(self):
        # LOG.info("Set Quantity sending keys");
        self.find(duck_quantity_input).clear()
        self.find(duck_quantity_input).send_keys(str(quantity_order))

    # @Step("Get Quantity value from Cart box")
    def get_quantity_from_cart(self):
        # LOG.info("Get Quantity value from Cart box");
        return self.find(cart_quantity).text

    # @Step("Size Options Menu click")
    def size_options_menu_click(self):
        # LOG.info("Size Options Menu click");
        self.find(size_options_menu).click()

    # @Step("Choosing small size")
    def choosing_small_size_duck(self, browser):
        # LOG.info("Choosing small size");
        self.size_options_menu_click()
        ActionChains(browser).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    # @Step("Choosing medium size")
    def choosing_medium_size_duck(self, browser):
        # LOG.info("Choosing medium size");
        self.size_options_menu_click()
        ActionChains(browser).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    # @Step("Choosing large size")
    def choosing_large_size_duck(self, browser):
        # LOG.info("Choosing large size");
        self.size_options_menu_click()
        ActionChains(browser).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    # @Step("Checking if Stock Status Available and choose Small Duck")
    def assert_stock_status_and_choose_small_duck(self, browser):
        # LOG.info("Checking if Stock Status Available and choose Small Duck");
        try:
            self.find(available_stock_status)
            self.size_options_menu_click()
            self.choosing_small_size_duck(browser)
        except NoSuchElementException:
            pass

    # @Step("Checking if Stock Status Available and choose Medium Duck")
    def assert_stock_status_and_choose_medium_duck(self, browser):
        # LOG.info("Checking if Stock Status Available and choose Medium Duck");
        try:
            self.find(available_stock_status)
            self.choosing_medium_size_duck(browser)
        except NoSuchElementException:
            pass

    # @Step("Checking if Stock Status Available and choose Large Duck")
    def assert_stock_status_and_choose_large_duck(self, browser):
        # LOG.info("Checking if Stock Status Available and choose Large Duck");
        try:
            self.find(available_stock_status)
            self.size_options_menu_click()
            self.choosing_large_size_duck(browser)
        except NoSuchElementException:
            pass

    # @Step("Checking correct submit button text")
    def get_add_to_cart_button_text(self):
        # LOG.info("Checking correct submit button text");
        return self.find(duck_quantity_submit_button).text

    # @Step("Getting Duck color from details")
    def get_duck_color_text_from_details(self):
        # LOG.info("Getting Duck color from details");
        return self.find(details_duck_body_color).text

