import requests

url = 'http://jisutianqi.market.alicloudapi.com/weather/query'
headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': 'APPCODE 你管理后台中查询到的appcode'
}
params = {'citycode': '101010100'}
r = requests.get(url, headers=headers, params=params)
print(r.json())
