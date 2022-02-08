import requests

sUrl = "https://www.baidu.com"

while True:
    r1 = requests.request("get", sUrl)
    print(r1.status_code)
    del r1
