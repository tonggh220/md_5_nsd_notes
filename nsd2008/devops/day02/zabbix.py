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
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
################################
# 获取Linux servers组的ID: 2
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
#     "auth": "b5479950bf43060f0035d68845b71d8f",
#     "id": 1
# }
################################
# 获取template os linux模板的信息, id: 10001
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
#     "auth": "b5479950bf43060f0035d68845b71d8f",
#     "id": 1
# }
################################
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web1",
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
    "auth": "b5479950bf43060f0035d68845b71d8f",
    "id": 1
}


################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
