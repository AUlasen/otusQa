import pytest


url = "http://192.168.56.103/opencart/"


def test_1(test_fixture):
    wd = test_fixture
    wd.get(url)
    logo_div = wd.find_element_by_id("logo")
    logo_a = logo_div.find_element_by_tag_name("a")
    logo_href = logo_a.get_attribute("href")
    assert logo_href.__contains__(url)


