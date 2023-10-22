""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By


class IndexPage(BaseObject, Assertions):
    """fff"""

    USERNAME_FIELD = (By.CSS_SELECTOR, ".input-container #username")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")
    LOGIN_BTN = (By.TAG_NAME, 'button')
    LOGOUT_BTN = (By.CLASS_NAME, 'logout-button')
    ERROR_TEXT = (By.XPATH, '//*[@id="message"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, login):
        """fff"""
        self.send_keys(self.USERNAME_FIELD, value=login)

    def enter_password(self, password):
        """fff"""
        self.send_keys(self.PASSWORD_FIELD, value=password)

    def click_to_login_btn(self):
        """click login"""
        self.click(self.LOGIN_BTN)

    def verify_login(self, text):
        """'''login '''"""
        self.assert_equal(self.get_text(self.LOGOUT_BTN), expected=text)

    def verify_incorrect_login(self, text):
        """'''login '''"""
        self.assert_equal(self.get_text(self.ERROR_TEXT), expected=text)
