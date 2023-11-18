""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By


class CheckboxesAndScroll(BaseObject, Assertions):
    """fff"""

    CHECKBOX_LIST = (By.CSS_SELECTOR, '.checkbox-list')
    SINGLE_CHECKBOX = lambda self, number: (By.CSS_SELECTOR,
                                            f'.checkbox-list li:nth-child({number}) > input[type=checkbox]')
    COUNTER = (By.ID, 'counter')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_checkbox(self, number):
        self.click(self.SINGLE_CHECKBOX(number))

    def counter_checkbox(self, checkbox_list):
        for i in range(1, checkbox_list + 1):
            self.click_checkbox(i)
            self.assert_equal(self.get_text(self.COUNTER), f'{i}')

    def counter_uncheck_checkbox(self, checkbox_list):
        for i in range(1, checkbox_list + 1):
            self.click_checkbox(i)
            self.assert_equal(self.get_text(self.COUNTER), f'{checkbox_list - i}')
