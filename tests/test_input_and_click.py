import selenium.webdriver.common.devtools.v85.debugger
from pytest import mark
import time


@mark.input_and_click
def test_enter_value(input_and_click_instance):
    input_and_click_instance.enter_items('1')
    input_and_click_instance.add_value()
    input_and_click_instance.enter_items('2')
    input_and_click_instance.add_value()
    input_and_click_instance.check_all(2)


# @mark.input_and_click
# def test_won(input_and_click_instance):
#     input_and_click_instance.enter_items('2')
#     input_and_click_instance.add_value()
#     input_and_click_instance.enter_items('1')
#     input_and_click_instance.add_value()
#     input_and_click_instance.delete_value()
#     input_and_click_instance.check_items('2')

@mark.test_one
def test_back_btn(input_and_click_instance, hover_and_select_instance):
    assert input_and_click_instance.click_back().check_marker() == 'SELECT'
    # assert hover_and_select_instance.check_marker == 'SELECT'
