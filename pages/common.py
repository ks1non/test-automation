""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By


class Common(BaseObject, Assertions):
    """fff"""

    THEME_DAY = (By.CLASS_NAME, 'day-mode')  # noqa
    THEME_NIGHT = (By.CLASS_NAME, 'day-mode night-mode')
    SWITCH = (By.XPATH, '//*[@id="addBtn"]')  # noqa
    BACK_BTN = (By.CLASS_NAME, 'back-button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_night_theme(self):
        self.is_visible(self.THEME_NIGHT)

    def check_day_theme(self):
        self.is_visible(self.THEME_DAY)

    def click_back(self):
        self.click(self.BACK_BTN)

    def click_swtch(self):
        self.click(self.SWITCH)

    def navigate_pages(self):
        pass