"""fff"""
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from support.logger import log_func

class BaseObject:
    """fff"""
    LOG = log_func()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)

    def all_visible(self, locator) -> WebElement:
        """fff"""
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def get_url(self):
        return self.driver.current_url

    def no_visible(self, locator) -> WebElement:
        """fff"""
        return self.wait.until_not(ec.visibility_of_element_located(locator))

    def is_visible(self, locator) -> WebElement:
        """fff"""
        self.LOG.info(f'{locator} is visible')
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator) -> WebElement:
        """fff"""
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        """fff"""
        self.is_clickable(locator).click()

    def send_keys(self, locator, value):
        """этот метод нужен что бы ввести текст"""
        self.is_visible(locator).send_keys(value)

    def get_text(self, locator):
        """fff"""
        return self.is_visible(locator).text

    def get_all(self, locator):
        """fff"""
        return self.all_visible(locator).text

    def items_in_list(self, locator):
        items_list = self.wait.until(ec.visibility_of_element_located(locator))
        items = items_list.text.split()
        return items

    def hover(self, locator):
        element = self.is_visible(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def dnd(self, locator_0, locator_1):
        drag = self.is_visible(locator_0)
        drop = self.is_visible(locator_1)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag, drop).perform()

