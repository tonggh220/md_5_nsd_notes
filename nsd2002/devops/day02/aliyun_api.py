import requests
import pprint

url = 'http://jisutqybmf.market.alicloudapi.com/weather/query'
params = {'citycode': '101010100'}
headers = {'Authorization': 'APPCODE 你的appcode', 'Content-Type': 'application/json; charset=UTF-8'}
r = requests.get(url, params=params, headers=headers)
# pprint.pprint(r.json())
data = r.json()
print(data['result']['city'])
pprint.pprint(data['result']['daily'][0])
pprint.pprint(data['result']['daily'][0]['day'])
