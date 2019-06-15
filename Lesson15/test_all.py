import random

import allure
import pytest

@allure.title("This test will be passed")
def test_pass():
    pass


@allure.title("This test will be failed")
def test_fail():
    assert False


@allure.title("This test will be broken")
def test_broken():
    raise ValueError("Some error")


@pytest.mark.flaky(reruns=15)
@allure.title("This test is flaky. It will be retried on fail.")
def test_with_retries():
    x = random.random()
    assert x < 0.2


@allure.title("This test contains steps.")
def test_with_steps():
    make_step1('User', 'Password')
    make_step2()
    make_step3()


@allure.step('Войти в систему под пользователем: "{0}", с паролем: "{1}"')
def make_step1(login, password):
    print('Просто добавь код')


@allure.step('Выполнить важные действия')
def make_step2():
    print('It is step 2')


@allure.step('Проверить, что все хорошо')
def make_step3():
    assert False

