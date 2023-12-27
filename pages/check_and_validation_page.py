""" test """
from support.assertions import Assertions
from base.base_objeckt import BaseObject
from selenium.webdriver.common.by import By
import allure


class CheckAndValidationPage(BaseObject, Assertions):
    """fff"""

    DATA_INPUT = (By.XPATH, '//*[@id="dataInput"]')
    VALIDATION_SQUARE = (By.XPATH, '//*[@id="validationSquare"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Вводим значение в инпут")
    def enter_value(self, value):
        self.send_keys(self.DATA_INPUT, value)

    @allure.step("проверяем вывод соответствующего сообщения")
    def validation_text(self, text):
        self.assert_text(self.get_text(self.VALIDATION_SQUARE), expected=text)
