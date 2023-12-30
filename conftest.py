import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage
from pages.check_and_validation_page import CheckAndValidationPage
from pages.input_and_click_page import InputAndClickPage
from pages.hover_and_select_page import HoverAndSelectPage
from pages.common import Common
from pages.drag_and_drop_page import DragAndDropPage
from pages.checkboxes_and_scroll_page import CheckboxesAndScroll
from pages.sort_by_page import SortByPage
import allure


@pytest.fixture(scope='function')
def get_chrome_options():
    '''scope рядом с каждой фекстурой , по дефолту фанкшен'''
    options = ChromeOptions()
    options.add_argument('headless')
    # options.add_argument('--start-maximized')
    return options


@pytest.fixture(scope='function')
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture(scope='function')
def index_page_instance(get_webdriver):
    get_webdriver.get('https://toghrulmirzayev.github.io/ui-simulator/')
    yield IndexPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function')
def check_and_validation_instance(get_webdriver):
    get_webdriver.get('https://toghrulmirzayev.github.io/ui-simulator/check_and_validate.html')
    yield CheckAndValidationPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function')
def input_and_click_instance(get_webdriver):
    get_webdriver.get('https://toghrulmirzayev.github.io/ui-simulator/input-and-click.html')
    yield InputAndClickPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function')
def hover_and_select_instance(get_webdriver):
    get_webdriver.get('https://toghrulmirzayev.github.io/ui-simulator/input-and-click.html')
    yield HoverAndSelectPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function')
def common_instance(get_webdriver):
    get_webdriver.get('https://toghrulmirzayev.github.io/ui-simulator/hover_and_select.html')
    yield Common(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function')
def drag_and_drop_instance(get_webdriver):
    get_webdriver.get('https://toghrulmirzayev.github.io/ui-simulator/drag-and-drop.html')
    yield DragAndDropPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function')
def checkboxes_and_scroll_instance(get_webdriver):
    get_webdriver.get('https://toghrulmirzayev.github.io/ui-simulator/checkbox-and-scroll.html')
    yield CheckboxesAndScroll(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function')
def setup_sorting_instance(get_webdriver):
    get_webdriver.get('https://toghrulmirzayev.github.io/ui-simulator/sorting.html')
    yield SortByPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failures(get_webdriver, request):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        test_case_name = request.node.name
        screenshot = 'screenshot_on_failures' + f'_{test_case_name}' + '.png'
        get_webdriver.get_screenshot_as_file(screenshot)
        allure.attach.file(screenshot, 'screenshot_on_failures.png', attachment_type=allure.attachment_type.PNG)
