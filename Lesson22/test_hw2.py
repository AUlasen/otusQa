from Lesson22.MyHttpClient import MyHttpRequest

req = MyHttpRequest(host="yandex.ru", use_ssl=True)
req.add_header('Accept-Language', 'fr')
resp = req.send()

print(resp.html_info['imgs'])
print(resp.html_info['links'])
print(resp.html_info['tags'])
print(resp.html_info['most_frequent_tags'])

