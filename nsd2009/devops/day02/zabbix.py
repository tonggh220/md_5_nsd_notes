import requests
import json

url = 'http://192.168.1.200/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
###################################
data = {
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
}
###################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
