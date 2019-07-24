
from Lesson22.MyHttpClient import MyHttpRequest

req = MyHttpRequest(host="yandex.ru", use_ssl=True)
req.add_header('Accept-Language', 'fr')
resp = req.send()
print(resp.text)
print(resp.http_ver)
print(resp.status_code)
print(resp.headers)
print(resp.body)