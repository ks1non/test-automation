""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By


class SortByPage(BaseObject, Assertions):
    """fff"""

    ITEMTABLE = (By.CSS_SELECTOR, '#myTable')  # noqa
    COLUMNSORT = lambda self, column: (By.CSS_SELECTOR, f'#myTable > thead > tr > th:nth-child({column})')  # noqa
    BODYTABLE = (By.CSS_SELECTOR, '#myTable > tbody')  # noqa
    HEADTABLE = (By.CSS_SELECTOR, '#myTable > thead')  # noqa
    SINGLE_ROW = lambda self, row, column: (By.CSS_SELECTOR,
                                            f'#myTable > tbody > tr:nth-child({row}) > td:nth-child({column})')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sorted_name_asc(self, row):
        expected = []
        actual = []
        for i in range(1, row + 1):
            expected.append(self.get_text(self.SINGLE_ROW(i, 1)))
        expected.sort()
        self.click(self.COLUMNSORT(1))
        for i in range(1, row + 1):
            actual.append(self.get_text(self.SINGLE_ROW(i, 1)))
        self.assert_equal(actual, expected)

    # def get_name_spisok(self):
    #     name_spisok = []
    #     for i in range(1, 9):
    #         name_spisok.append(self.SINGLE_ROW(i, 1))
    #
    # def get_age_spisok(self):
    #     age_spisok = []
    #     for i in range(1, 9):
    #         age_spisok.append(self.get_text(self.SINGLE_ROW(i, 2)))
    #
    # def get_role_spisok(self):
    #     role_spisok = []
    #     for i in range(1, 9):
    #         role_spisok.append(self.SINGLE_ROW(i, 1))
