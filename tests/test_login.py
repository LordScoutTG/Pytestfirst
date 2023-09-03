import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.home_page import HomePage
from page.login_page import LoginPage
from tests.conftest import driver

delay = 3


class TestLogin:

    correct_login_email = "1123@123.com"
    correct_login_password = "adDA12341"

    def test_button1_exist(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        assert login_page.sign_in_button_find().is_displayed()

    def test_login_field_exist(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.sign_in_button_find().click()
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable(login_page.email_input_box))
        assert login_page.email_input.is_displayed()

    @allure.story("Login tests")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Login with correct creds")
    def test_success_login_test(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        login_page.open()
        logging.debug("Attempting login with correct creds")
        login_page.attempt_login(TestLogin.correct_login_email, TestLogin.correct_login_password, driver)
        assert (home_page.success_message_is_visible(), "Login was not successful")

    @allure.story("Login tests")
    @allure.description("Login with incorrect creds")
    def test_unsuccessful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        logging.debug("Attempting login with incorrect creds")
        login_page.attempt_login("vadim.zubovich@gmail.com", "Test1234!", driver)
        assert (login_page.un_success_message_is_visible(), "Unsuccessful Login")
