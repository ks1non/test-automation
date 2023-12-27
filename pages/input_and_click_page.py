""" test """
import allure
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

    @allure.step("Вводим значение в инпут")
    def enter_items(self, value):
        """Вводим значение в инпут"""  # noqa
        self.send_keys(self.INPUTTEXT, value)

    @allure.step("Нажимаем кнопку 'добавить значение'")
    def add_value(self):
        """Нажимаем кнопку Add - добавляем значение"""  # noqa
        self.click(self.ADDBTN)

    @allure.step("Нажимаем delete - удаляем последнее добавленное значение")
    def delete_value(self):
        """Нажимаем delete - удаляем последнее добавленное значение"""  # noqa
        self.click(self.DELETEBTN)

    @allure.step("проверяем что добавленное значение совпадает с ожидаемым")
    def check_items(self, items):
        """проверяем что добавленное значение совпадает с ожидаемым"""  # noqa
        self.assert_equal(self.get_text(self.ITEMS), items)

    @allure.step("Проверяем наличие всех значений")
    def check_all(self, items):
        """Проверяем наличие всех значений"""
        self.assert_equal(self.items_in_list(self.ITEMS), items)

    @allure.step("добавляем несколько значений")
    def add_all_value(self, items):
        for i in items:
            self.enter_items(i)
            self.add_value()
