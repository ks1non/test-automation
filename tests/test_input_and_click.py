from pytest import mark


@mark.input_and_click
def test_del_value(input_and_click_instance):
    input_and_click_instance.add_all_value(['1', '2'])
    input_and_click_instance.delete_value()
    input_and_click_instance.check_all(['1'])


@mark.input_and_click
def test_adding_multiple_values(input_and_click_instance):
    input_and_click_instance.add_all_value(['1', '2', '3'])
    input_and_click_instance.check_all(['1', '2', '3'])
