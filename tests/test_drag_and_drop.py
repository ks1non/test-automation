from pytest import mark


elements_list = [("3", "1"), ("3", "2"), ("7", "3"), ("5", "4"), ("7", "6")]

@mark.test_dnd
def test_dnd(drag_and_drop_instance):
    drag_and_drop_instance.replace_cards(elements_list)
    drag_and_drop_instance.verify_dnd()
