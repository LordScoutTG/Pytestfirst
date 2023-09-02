from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def browser():


    options = Options()
    options.add_argument('--headless=new')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    # chrome_option = ChromeOption()
    # chrome_option.add_argument('--headless')
    # chrome_option.add_argument("--window-size=1920,1080")
    return chrome_browser


@pytest.fixture()
def duck_name(duck_name):
    return duck_name.param
