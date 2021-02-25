import requests
import json

url = 'http://192.168.1.200/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
###################################
# 对于不需要认证即可获得的信息，可以直接查
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }
###################################
# 获取隐私信息，需要token。获取用户的token:
# e25d9a0294c815385d727aa14b66f338
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}


###################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
