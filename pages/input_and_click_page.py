""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By
from pages.hover_and_select_page import HoverAndSelectPage


class InputAndClickPage(BaseObject, Assertions):
    """fff"""

    INPUTTEXT = (By.XPATH, '//*[@id="inputText"]')  # noqa
    ADDBTN = (By.XPATH, '//*[@id="addBtn"]')  # noqa
    DELETEBTN = (By.XPATH, '//*[@id="deleteBtn"]')  # noqa
    ITEMS = (By.XPATH, '//*[@id="items"]')
    BACK_BTN = (By.XPATH, '/html/body/div[3]/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_back(self):
        self.click(self.BACK_BTN)

    def enter_items(self, value):
        """Вводим значение в инпут"""  # noqa
        self.send_keys(self.INPUTTEXT, value)

    def add_value(self):
        """Нажимаем кнопку Add - добавляем значение"""  # noqa
        self.click(self.ADDBTN)

    def delete_value(self):
        """Нажимаем delete - удаляем последнее добавленное значение"""  # noqa
        self.click(self.DELETEBTN)

    def check_items(self, items):
        """проверяем что добавленное значение совпадает с ожидаемым"""  # noqa
        self.assert_equal(self.get_text(self.ITEMS), items)

    def check_all(self, items):
        """Проверяем наличие всех значений"""
        self.assert_equal(self.get_all(self.ITEMS), items)
