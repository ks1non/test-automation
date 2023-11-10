from pytest import mark



@mark.input_and_click
def test_enter_value(input_and_click_instance):
    input_and_click_instance.enter_items(1)
    input_and_click_instance.add_value()
    input_and_click_instance.enter_items(2)
    input_and_click_instance.add_value()
    input_and_click_instance.check_all(['1', '2'])

@mark.input_and_click
def test_won(input_and_click_instance):
    input_and_click_instance.enter_items('2')
    input_and_click_instance.add_value()
    input_and_click_instance.enter_items('1')
    input_and_click_instance.add_value()
    input_and_click_instance.delete_value()
    input_and_click_instance.check_items('2')


