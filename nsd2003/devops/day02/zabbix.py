import requests
import json

url = 'http://192.168.1.154/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
##################################
# 对于不需要认证即可获得的信息，可以直接查
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1  # 随便指定一个数字，表示作业ID
# }
##################################
# 获取隐私信息，需要token。获取用户的token: 7e811a3f758ccbdcaba211d1431bac47
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
# 查询组，获取组id: 2
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
    "auth": "7e811a3f758ccbdcaba211d1431bac47",
    "id": 1
}
##################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 只关心result对应的部分

