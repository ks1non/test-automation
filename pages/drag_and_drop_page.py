""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By


class DragAndDropPage(BaseObject, Assertions):
    """fff"""

    ITEM = lambda self, item: (By.CSS_SELECTOR, f'.container div:nth-child({item})')
    DONE_TEXT = (By.CSS_SELECTOR, '.done')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def replace_cards(self, elements_list):
        elements = elements_list
        for source, target in elements:
            self.dnd(self.ITEM(source), self.ITEM(target))

    def verify_dnd(self):
        self.assert_equal(self.get_text(self.DONE_TEXT), 'DONE')
