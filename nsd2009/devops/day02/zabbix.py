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
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
###################################
# 查询组，获取Linux servers组id: 2
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
#     "auth": "e25d9a0294c815385d727aa14b66f338",  # 上一步获取的令牌
#     "id": 1
# }
##################################
# 获取Template OS Linux模板信息, id: 10001
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
#     "auth": "e25d9a0294c815385d727aa14b66f338",
#     "id": 1
# }
##################################
# 新建名为web1的主机，在Linux servers组中，应用Template os linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web1",  # 创建的主机名
        "interfaces": [  # 主机IP地址等信息
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
    "auth": "e25d9a0294c815385d727aa14b66f338",
    "id": 1
}


###################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
