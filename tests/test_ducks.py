import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
correctLoginEmail = "1123@123.com"
correctLoginPassword = "adDA12341"


@pytest.fixture(scope='function', autouse=True)
def f_wrapper_function(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.attemptLogin(correctLoginEmail, correctLoginPassword, browser)

# class DucksTest(BasePage):

    # @Test(description = "Checking correct sticker Sale placing")
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")
    # def successSaleStickerOnDuck():
        # LOG.debug("Comparing if every Sale duck is YELLOW");
        # HomePage.searchDucksWithOnSaleSticker().forEach(x -> Assert.assertEquals(x.getText(), Duck.YELLOWDUCK.value));

    # @Test(dataProvider = "duckDataProvider", dataProviderClass = DataProviderClass.class)
    # @Severity(SeverityLevel.NORMAL)
    # @Story("Ducks shopping tests")


def test_success_main_page_most_popular_duck_click(duckName, browser):
    home_page = HomePage(browser)
        # LOG.debug("Checking correct click on most popular duck at Main Page");
    home_page.clickOnMostPopularDuck(duckName, browser)
    assert home_page.duckTitleIsCorrect() == duckName
