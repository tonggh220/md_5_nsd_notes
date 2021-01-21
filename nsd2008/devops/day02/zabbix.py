import json
import requests

url = 'http://192.168.1.100/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
################################
# 非隐私数据可以直接访问
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }
################################
# 获取用户的token: b5479950bf43060f0035d68845b71d8f
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}



################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
