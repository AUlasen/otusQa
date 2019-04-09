import requests

breweries_url = "https://api.openbrewerydb.org/breweries"
breweries_endpoints = ["","?by_state=new_york", "?by_name=cooper", "5494"]


def test_breweries_api(endpoint):
    url = "".join([breweries_url, endpoint])
    print(url)
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers['Content-type'].__contains__("application/json")

test_breweries_api("")