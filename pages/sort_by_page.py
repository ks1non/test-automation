""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By


class SortByPage(BaseObject, Assertions):
    """fff"""

    ITEMTABLE = (By.ID, 'myTable')  # noqa
    NAMEASC = (By.CSS_SELECTOR, '#myTable > thead > tr > th:nth-child(1).asc')      # noqa
    AGEASC = (By.CSS_SELECTOR, '#myTable > thead > tr > th:nth-child(2).asc')       # noqa
    ROLEASC = (By.CSS_SELECTOR, '#myTable > thead > tr > th:nth-child(3).asc')      # noqa
    NAMEDESC = (By.CSS_SELECTOR, '#myTable > thead > tr > th:nth-child(1).desc')    # noqa
    AGEDESC = (By.CSS_SELECTOR, '#myTable > thead > tr > th:nth-child(2).desc')     # noqa
    ROLEDESC = (By.CSS_SELECTOR, '#myTable > thead > tr > th:nth-child(3).desc')    # noqa
    BODYTABLE = (By.XPATH, '//*[@id="myTable"]/tbody')                              # noqa
    HEADTABLE = (By.XPATH, '//*[@id="myTable"]/thead')                              # noqa

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
