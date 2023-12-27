"""Тут происходит вызов тестов с разными параметрами"""  # noqa
import pytest
from pytest import mark
from env_setup import login, password
import allure

incorrect_1 = ['', '', 'Username and password fields cannot be empty']
incorrect_2 = ['correct_username', 'correct_username', 'Password or username is incorrect']
incorrect_3 = ['correct_username', '', 'Password field cannot be empty']
incorrect_4 = ['', 'correct_username', 'Username field cannot be empty']


@allure.description('Success login')
@allure.label('owner', 'Sergey')
@allure.title('Successful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
@mark.smoke
def test_success_login(index_page_instance):
    index_page_instance.enter_username(login)
    index_page_instance.enter_password(password)
    index_page_instance.click_to_login_btn()
    index_page_instance.verify_login('Log out')


@allure.description('Unsuccess login')
@allure.label('owner', 'Sergey')
@allure.title('Unsuccessful login')
@allure.suite('Authorization suite')
@mark.index
@pytest.mark.parametrize('un_login, un_password, un_text', (incorrect_1, incorrect_2, incorrect_3, incorrect_4))
def test_unsuccessful_login(index_page_instance, un_login, un_password, un_text):
    index_page_instance.enter_username(un_login)
    index_page_instance.enter_password(un_password)
    index_page_instance.click_to_login_btn()
    index_page_instance.verify_incorrect_login(un_text)
