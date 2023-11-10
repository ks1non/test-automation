""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By


class HoverAndSelectPage(BaseObject, Assertions):
    """fff"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    MARKERHOVERPAGES = (By.CLASS_NAME, 'select-text')  # noqa

    def check_marker(self):
        self.get_text(self.MARKERHOVERPAGES)
