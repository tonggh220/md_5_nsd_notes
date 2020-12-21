import requests
import json

url = 'http://192.168.1.101/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
