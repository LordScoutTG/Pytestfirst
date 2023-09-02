import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.main_menu import MainMenu
from pages.rubber_duck_page import RubberDucksPage
from tests.conftest import duck_name

correct_login_email = "1123@123.com"
correct_login_password = "adDA12341"
currency_selector = (By.CSS_SELECTOR, "[name='currency_code']")
euro_price_symbols = (By.CSS_SELECTOR, "[class$='price']")
duck_quantity_submit_button_text = "Add To Cart"
delay = 3

@pytest.fixture(scope='function', autouse=True)
def f_wrapper_function(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.attempt_login(correct_login_email, correct_login_password, browser)

# class DucksTest(BasePage):

    # @Test(description = "Checking correct sticker Sale placing")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")
def test_success_sale_sticker_on_duck(browser):
    home_page = HomePage(browser)
        # LOG.debug("Comparing if every Sale duck is YELLOW");
    for i in range(len(home_page.search_ducks_with_on_sale_sticker())):
        assert home_page.search_ducks_with_on_sale_sticker()[i].text == "Yellow Duck"

    # @Test(description="Checking correct lower price for Sale ducks")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")


def test_success_cheaper_price_on_sale_duck(browser):
    home_page = HomePage(browser)
    for i in range(len(home_page.search_ducks_with_cheaper_price())):
        assert home_page.search_ducks_with_cheaper_price()[i].text == "Yellow Duck"
    # LOG.debug("Comparing if every cheap price duck is YELLOW");


    # @Test(dataProvider = "duckDataProvider", dataProviderClass = DataProviderClass.class)
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")
@pytest.mark.parametrize('duck_name', ["Yellow Duck", "Red Duck", "Blue Duck", "Green Duck", "Purple Duck"])
def test_success_main_page_most_popular_duck_click(duck_name, browser):
    home_page = HomePage(browser)
    # LOG.debug("Checking correct click on most popular duck at Main Page");
    home_page.click_on_most_popular_duck(duck_name, browser)
    assert home_page.duck_title_is_correct() == duck_name

    # @Test(description = "Checking currency change from USD to EURO")
    # @Severity(SeverityLevel.CRITICAL)
    # @Story("Currency Tests")
def test_success_currency_change(browser):
    home_page = HomePage(browser)
    home_page.reg_settings_change_link_click()
    WebDriverWait(browser, delay).until(EC.presence_of_element_located(currency_selector))
        # LOG.debug("Waiting for currency selector appeared");
    home_page.currency_selector_click()
        # LOG.debug("Choosing EURO by clicking keys");
    ActionChains(browser).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    home_page.submit_settings_button_click()
        # LOG.debug("Waiting for elements on page appeared after saving");
    WebDriverWait(browser, delay).until(EC.presence_of_element_located(euro_price_symbols))
    for i in range(len(home_page.search_euro_price_symbols())):
        assert "\u20AC" in home_page.search_euro_price_symbols()[i].text

    # @Test(dataProvider = "duckDataProvider", dataProviderClass = DataProviderClass.class)
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")
@pytest.mark.parametrize('duck_name', ["Yellow Duck", "Red Duck", "Blue Duck", "Green Duck", "Purple Duck"])
def test_success_duck_page_click(duck_name, browser):
        main_menu = MainMenu(browser)
        rubber_ducks_page = RubberDucksPage(browser)
        home_page = HomePage(browser)
        # LOG.info("Checking correct click on duck at Duck Page");
        main_menu.click_main_menu_rd_link(browser)
        rubber_ducks_page.click_on_duck(duck_name)
        assert home_page.duck_title_is_correct() == duck_name

    # @Test(dataProvider = "duckDataProvider", dataProviderClass = DataProviderClass.class)
    # @Severity(SeverityLevel.MINOR)
    # @Story("Ducks shopping tests")

def test_success_add_to_cart_button_text(browser):
        # LOG.info("Checking correct Add To Cart button text");
        main_menu = MainMenu(browser)
        rubber_ducks_page = RubberDucksPage(browser)
        main_menu.click_main_menu_rd_link(browser)
        rubber_ducks_page.click_on_duck("Yellow Duck")
        assert rubber_ducks_page.get_add_to_cart_button_text() == duck_quantity_submit_button_text


    # @Test(dataProvider = "duckDataProvider", dataProviderClass = DataProviderClass.class)
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")
def test_success_duck_arrow_up_quantity(browser):
        # LOG.info("Checking correct click arrow UP Quantity at Duck Page");
        main_menu = MainMenu(browser)
        rubber_ducks_page = RubberDucksPage(browser)
        main_menu.click_main_menu_rd_link(browser)
        rubber_ducks_page.click_on_duck("Yellow Duck")
        rubber_ducks_page.click_on_quantity_input()
        for i in range(3):
            ActionChains(browser).send_keys(Keys.ARROW_UP).perform()
            assert rubber_ducks_page.get_quantity_from_input(browser) == i + 2


    # @Test(dataProvider = "duckDataProvider", dataProviderClass = DataProviderClass.class)
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")
    # @Flaky
@pytest.mark.parametrize('duck_name', ["Yellow Duck", "Red Duck", "Blue Duck", "Green Duck", "Purple Duck"])
def test_success_duck_dend_keys_quantity(duck_name, browser):
        # LOG.debug("Checking correct sending keys to Quantity at Duck Page");
        main_menu = MainMenu(browser)
        rubber_ducks_page = RubberDucksPage(browser)
        home_page = HomePage(browser)
        cart_page = CartPage(browser)
        main_menu.click_main_menu_rd_link(browser)
        rubber_ducks_page.click_on_duck(duck_name)
        rubber_ducks_page.set_quantity_by_keys()
        rubber_ducks_page.assert_stock_status_and_choose_large_duck(browser)
        rubber_ducks_page.click_on_duck_quantity_submit()
        WebDriverWait(browser, delay).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class=\"badge quantity\"]"), "10"))
        assert rubber_ducks_page.get_quantity_from_cart() == "10"
        home_page.click_on_cart_button()
        cart_page.cleaning_cart(browser)

    # @Test(dataProvider = "duckDataProvider", dataProviderClass = DataProviderClass.class)
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")
@pytest.mark.parametrize('duck_name', ["Yellow Duck", "Red Duck", "Blue Duck", "Green Duck", "Purple Duck"])
def test_success_duck_detail_color(duck_name, browser):
        # LOG.info("Checking correct duck details color");
        main_menu = MainMenu(browser)
        rubber_ducks_page = RubberDucksPage(browser)
        main_menu.click_main_menu_rd_link(browser)
        rubber_ducks_page.click_on_duck(duck_name)
        assert rubber_ducks_page.get_duck_color_text_from_details() == duck_name.split()[0]


