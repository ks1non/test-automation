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
    SELECT = (By.CLASS_NAME, 'select-text')
    DROP_DOWN = lambda self, index: (By.CSS_SELECTOR, f'.dropdown-content li:nth-child({index})')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_night_theme(self):
        self.is_visible(self.THEME_NIGHT)

    def check_day_theme(self):
        self.is_visible(self.THEME_DAY)

    def click_swtch(self):
        self.click(self.SWITCH)

    def _click_back(self):
        self.click(self.BACK_BTN)

    def _hover_to_select(self):
        self.hover(self.SELECT)

    def _select_pages_by_index(self, index):
        self.click(self.DROP_DOWN(index))

    def navigate_pages(self, page_index, url_list):
        for i in range(1, page_index + 1):
            self._hover_to_select()
            self._select_pages_by_index(i)
            self.assert_equal(url_list[i - 1], self.get_url())
            self._click_back()
            self.assert_equal(self.get_url(),
                              'https://toghrulmirzayev.github.io/ui-simulator/hover_and_select.html')

    def navigate_pages_parametrize(self, index, url):
        self._hover_to_select()
        self._select_pages_by_index(index)
        self.assert_equal(url, self.get_url())
        self._click_back()
        self.assert_equal(self.get_url(),
                          'https://toghrulmirzayev.github.io/ui-simulator/hover_and_select.html')
