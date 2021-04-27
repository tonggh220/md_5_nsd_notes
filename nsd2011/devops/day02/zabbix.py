import requests
import json

url = 'http://192.168.1.100/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
######################################
# 对于不需要认证即可获得的信息，可以直接查
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }
##################################
# 获取隐私信息，需要token。
# 获取用户的token: 10b50e8ba54728a0b976fc1ce3ea74c5
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
##################################
# 查询组，获取Linux servers组ID: 2
data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
                # "Zabbix servers",
                "Linux servers"
            ]
        }
    },
    "auth": "10b50e8ba54728a0b976fc1ce3ea74c5",
    "id": 1
}
##################################
# 获取Template os linux模板信息

######################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 只关心result对应的部分

