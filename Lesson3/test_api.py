import random

import pytest
import requests

dog_api_url = ("https://dog.ceo/api")

dog_api_endpoints = ["breeds/list/all", "breeds/image/random",
                     "breeds/image/random/3", "breed/hound/images",
                     "breed/hound/images/random", "breed/hound/images/random/3",
                     "breed/hound/list", "breed/hound/afghan/images"]

@pytest.fixture(scope="session", autouse=True)
def session_fixture(request):
    print('\nSession was started')

    def session_fin():
        print('\nSesion was finished')

    request.addfinalizer(session_fin)



@pytest.mark.parametrize("endpoint", dog_api_endpoints)
def test_dog_api(endpoint):
    url = "/".join([dog_api_url, endpoint])
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json"

breweries_url = "https://api.openbrewerydb.org/breweries"
breweries_endpoints = ["","?by_state=new_york", "?by_name=cooper", "/5494"]

@pytest.mark.parametrize("endpoint", breweries_endpoints)
def test_breweries_api(endpoint):
    url = "".join([breweries_url, endpoint])
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers['Content-type'].__contains__("application/json")

cdnjs_url = "https://api.cdnjs.com"
cdnjs_endpoints = [("libraries","application/json"), ("libraries?output=human","text/html"), ("libraries?search=jquery&output=human","text/html")]

@pytest.mark.parametrize("endpoint, content_type", cdnjs_endpoints)
def test_cdnjs_api(endpoint, content_type):
    url = "/".join([cdnjs_url, endpoint])
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers['Content-type'].__contains__(content_type)