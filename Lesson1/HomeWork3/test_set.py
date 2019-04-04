"""Home Work 3 Lesson 1"""
import pytest


@pytest.mark.usefixtures('test_fixture')
def test_1():
    """Check length of the list after pop"""
    lst = [x for x in range(10)]
    lst.pop()
    assert lst.__len__() == 9

@pytest.mark.usefixtures('test_fixture')
def test_2():
    """Check dictionary values sum"""
    dic = {'first': 111, 'second': 222, 'third': 333}
    summm = 0
    for key in dic.keys():
        summm += dic.get(key)
    assert summm == 666

@pytest.mark.usefixtures('test_fixture')
def test_3():
    """String immutability"""
    str1 = 'string'
    str2 = str1.capitalize()
    assert (str1 == 'string') & (str2 == 'String')

@pytest.mark.usefixtures('test_fixture')
def test_4():
    """Check variable links"""
    lst1 = [x for x in range(10)]
    lst2 = lst1
    lst2.clear()
    assert lst1.__len__() == 0

@pytest.mark.usefixtures('test_fixture')
def test_5():
    """Check list iterator"""
    lst = [x for x in range(10)]
    lst_iterator = lst.__iter__()
    for i in lst:
        print(lst[i])
        assert lst[i] == lst_iterator.__next__()

@pytest.mark.usefixtures('test_fixture')
def test_6():
    """Check byte encode & decode"""
    b_0 = b'012345'
    b_1 = b_0.decode('utf-8').encode('utf-8')
    assert b_0 == b_1

@pytest.mark.usefixtures('test_fixture')
def test_7():
    """Check variable links"""
    str1 = 'Hello'
    str2 = 'World!'
    res = str1 + ' ' + str2
    assert res == 'Hello World!'

