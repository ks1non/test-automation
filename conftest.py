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

@pytest.fixture(scope='function')
def get_chrome_options():
    '''scope рядом с каждой фекстурой , по дефолту фанкшен'''
    options = ChromeOptions()
    # options.add_argument('headless')
    return options


@pytest.fixture(scope='function')
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture(scope='function')
def setup_index(get_webdriver):
    url = 'https://toghrulmirzayev.github.io/ui-simulator/'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()


@pytest.fixture(scope='function')
def index_page_instance(setup_index):
    yield IndexPage(setup_index)


@pytest.fixture(scope='function')
def setup_check_and_validation(get_webdriver):
    url = 'https://toghrulmirzayev.github.io/ui-simulator/check_and_validate.html'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()


@pytest.fixture(scope='function')
def check_and_validation_instance(setup_check_and_validation):
    yield CheckAndValidationPage(setup_check_and_validation)


@pytest.fixture(scope='function')
def setup_input_and_click(get_webdriver):
    url = 'https://toghrulmirzayev.github.io/ui-simulator/input-and-click.html'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()


@pytest.fixture(scope='function')
def input_and_click_instance(setup_input_and_click):
    yield InputAndClickPage(setup_input_and_click)


@pytest.fixture(scope='function')
def setup_hover_and_select(get_webdriver):
    url = 'https://toghrulmirzayev.github.io/ui-simulator/hover_and_select.html'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()


@pytest.fixture(scope='function')
def hover_and_select_instance(setup_hover_and_select):
    yield HoverAndSelectPage(setup_hover_and_select)


@pytest.fixture(scope='function')
def common_instance(setup_hover_and_select):
    yield Common(setup_hover_and_select)


@pytest.fixture(scope='function')
def setup_drag_and_drop(get_webdriver):
    url = 'https://toghrulmirzayev.github.io/ui-simulator/drag-and-drop.html'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()


@pytest.fixture(scope='function')
def drag_and_drop_instance(setup_drag_and_drop):
    yield DragAndDropPage(setup_drag_and_drop)


@pytest.fixture(scope='function')
def setup_checkboxes_and_scroll(get_webdriver):
    url = 'https://toghrulmirzayev.github.io/ui-simulator/checkbox-and-scroll.html'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()


@pytest.fixture(scope='function')
def checkboxes_and_scroll_instance(setup_checkboxes_and_scroll):
    yield CheckboxesAndScroll(setup_checkboxes_and_scroll)
