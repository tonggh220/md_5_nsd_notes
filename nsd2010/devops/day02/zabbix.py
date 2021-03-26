import requests
import json

url = 'http://192.168.1.100/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
#####################################
# 对于可以公开的数据，直接可以获取，如版本号
data = {
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
}
#####################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 主要关心result部分
