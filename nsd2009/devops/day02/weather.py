import requests
import pprint

url = 'http://jisutianqi.market.alicloudapi.com/weather/query'
headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': 'APPCODE 369deb7e22cc4808b2a5a5ba3effbb7e'
}
params = {'citycode': '101010100'}
r = requests.get(url, headers=headers, params=params)
pprint.pprint(r.json())
