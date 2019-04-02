"""Home Work 3 Lesson 1"""


def test_1(test_fixture):
    """Check length of the list after pop"""
    lst = [x for x in range(10)]
    lst.pop()
    assert lst.__len__() == 9


def test_4(test_fixture):
    """Check variable links"""
    lst1 = [x for x in range(10)]
    lst2 = lst1
    lst2.clear()
    assert lst1.__len__() == 0


def test_2(test_fixture):
    """Check dictionary values sum"""
    dic = {'first': 111, 'second': 222, 'third': 333}
    summm = 0
    for key in dic.keys():
        summm += dic.get(key)
    assert summm == 666


def test_3(test_fixture):
    """String immutability"""
    str1 = 'string'
    str2 = str1.capitalize()
    assert (str1 == 'string') & (str2 == 'String')
