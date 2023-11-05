"""Тут происходит вызов тестов с разными параметрами"""  # noqa
import pytest
from pytest import mark

correct_0 = ['correct_username', 'correct_password', 'Log out']
incorrect_1 = ['', '', 'Username and password fields cannot be empty']
incorrect_2 = ['correct_username', 'correct_username', 'Password or username is incorrect']
incorrect_3 = ['correct_username', '', 'Password field cannot be empty']
incorrect_4 = ['', 'correct_username', 'Username field cannot be empty']


@mark.index
def test_success_login(index_page_instance):
    index_page_instance.enter_username('correct_username')
    index_page_instance.enter_password('correct_password')
    index_page_instance.click_to_login_btn()
    index_page_instance.verify_login('Log out')


@mark.index
@pytest.mark.parametrize('login, password, text', (incorrect_1, incorrect_2, incorrect_3, incorrect_4),
                         )
def test_unsuccessful_login(index_page_instance, login, password, text):
    index_page_instance.enter_username(login)
    index_page_instance.enter_password(password)
    index_page_instance.click_to_login_btn()
    index_page_instance.verify_incorrect_login(text)
