import requests
import json

url = 'http://192.168.1.100/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
#####################################
# 对于可以公开的数据，直接可以获取，如版本号
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }
#####################################
# 通过用户名和密码获取用户令牌token: c8e616d93a8ca050975a9d4e9921d28c
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
#####################################
# 需要权限的资源，必须使用token才能访问
# 获取所有的主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [  # 获取所有主机信息
#                 # "Zabbix server",
#                 # "Linux server"
#             ]
#         }
#     },
#     "auth": "c8e616d93a8ca050975a9d4e9921d28c",
#     "id": 1
# }
#####################################
# 获取Linux servers主机组的id  'groupid': '2'
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
#     "auth": "c8e616d93a8ca050975a9d4e9921d28c",
#     "id": 1
# }
#####################################
# 获取template os linux模板的信息  'templateid': '10001'
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
#     "auth": "c8e616d93a8ca050975a9d4e9921d28c",
#     "id": 1
# }
#####################################
# 创建一台名为web1的主机，加入到Linux servers组中，应用template os linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web1",
        "interfaces": [  # 使用什么方式进行监控
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.2",
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
    "auth": "c8e616d93a8ca050975a9d4e9921d28c",
    "id": 1
}
#####################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 主要关心result部分
