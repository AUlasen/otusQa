
import pytest
import requests

site_url = "https://dog.ceo/api"
random_count_list = [x for x in range(1, 3)]


#@pytest.mark.usefixtures('test_fixture')
def test_random_img():
    """test"""
    endpoint = "breeds/image/random"
    url = "/".join([site_url, endpoint])
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json"


def test_random_img_data():
    """test"""
    endpoint = "breeds/image/random"
    url = "/".join([site_url, endpoint])
    response = requests.get(url)

    json_data = response.json()

    assert json_data['status'] == "success"
    img_url = json_data['message']

    response = requests.get(img_url)
    assert response.status_code == 200
    assert response.headers['Content-type'].startswith("image")


@pytest.mark.parametrize("count", random_count_list)
def test_random_img_multiple(count):
    """test"""
    endpoint = "breeds/image/random"
    str_count = str(count)
    url = "/".join([site_url, endpoint, str_count])
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json"


@pytest.mark.parametrize("count", random_count_list)
def test_random_img_multiple_data(count):
    """test"""
    endpoint = "breeds/image/random"
    str_count = str(count)
    url = "/".join([site_url, endpoint, str_count])
    response = requests.get(url)

    json_data = response.json()

    assert json_data['status'] == "success"

    img_list = json_data['message']

    assert img_list.__len__() == count

    for img_url in img_list:
        response = requests.get(img_url)
        assert response.status_code == 200
        assert response.headers['Content-type'].startswith("image")


