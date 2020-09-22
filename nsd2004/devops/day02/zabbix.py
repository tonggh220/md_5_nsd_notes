import requests
import json

url = 'http://192.168.1.161/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
########################################
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 101
# }
#######################################
# 获取token: d8d49f290e11ee1b9ad9bbbb83c25221
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
#######################################
# 获取linux servers组的信息  'groupid': '2'
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 # "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "d8d49f290e11ee1b9ad9bbbb83c25221",
#     "id": 1
# }
#######################################
# 获取template os linux模板信息  'templateid': '10001'
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "d8d49f290e11ee1b9ad9bbbb83c25221",
#     "id": 1
# }
#######################################
# 创建名为web2的主机，加入linux servers组中，使用template os linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web2",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.10",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "d8d49f290e11ee1b9ad9bbbb83c25221",
    "id": 1
}


r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
