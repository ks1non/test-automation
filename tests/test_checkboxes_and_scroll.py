from pytest import mark

@mark.checkbox_and_scroll
def test_checkbox_click(checkboxes_and_scroll_instance):
    checkboxes_and_scroll_instance.counter_checkbox(15)
