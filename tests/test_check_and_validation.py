import pytest
from pytest import mark

correct = ['15', 'Valid']
incorrect_1 = ['1', 'Not in range']
incorrect_2 = ['h', 'Not a number']
incorrect_3 = ['-1', 'Negative integer']
incorrect_test = ['15', 'Negative integer']


@mark.check_and_validation
@pytest.mark.parametrize('value, text', (correct, incorrect_1, incorrect_2, incorrect_3, incorrect_test))
def test_validation(check_and_validation_instance, value, text):
    check_and_validation_instance.enter_value(value)
    check_and_validation_instance.validation_text(text)
