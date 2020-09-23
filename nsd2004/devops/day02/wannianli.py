import requests

url = 'http://jisuwnl.market.alicloudapi.com/calendar/query'
headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': 'APPCODE xxxx'}
params = {'date': '2020-09-23'}
r = requests.get(url, headers=headers, params=params)
print(r.json())
