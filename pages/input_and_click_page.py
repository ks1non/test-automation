""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By


class InputAndClickPage(BaseObject, Assertions):
    """fff"""

    INPUTTEXT = (By.XPATH, '//*[@id="inputText"]')  # noqa
    ADDBTN = (By.XPATH, '//*[@id="addBtn"]')  # noqa
    DELETEBTN = (By.XPATH, '//*[@id="deleteBtn"]')  # noqa
    ITEMS = (By.XPATH, '//*[@id="items"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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