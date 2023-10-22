"""fff"""
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BaseObject:
    """fff"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_visible(self, locator) -> WebElement:
        """fff"""
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator) -> WebElement:
        """fff"""
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        """fff"""
        self.is_clickable(locator).click()

    def send_keys(self, locator, value):
        """fff"""
        self.is_visible(locator).send_keys(value)

    def get_text(self, locator):
        """fff"""
        return self.is_visible(locator).text
