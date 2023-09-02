import logging

import allure
from selenium.webdriver.common.by import By
from page.base_page import BasePage

edit_account_title = (By.CSS_SELECTOR, "h2[class=\"card-title\"]")
edit_account_title_text = "Account"


class EditAccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Getting Title Edit Account Page")
    def get_edit_account_title(self):
        logging.info('Getting Title Edit Account Page')
        return self.find(edit_account_title).text
