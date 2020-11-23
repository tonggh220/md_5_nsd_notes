import requests
import json

url = 'http://192.168.1.11/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
###################################
# 公开数据可以直接查询
# data = {
#     "jsonrpc": "2.0",  # 固定内容
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 101  # 随便指定一个数字，表示作业ID
# }
###################################
# 获取admin用户的token: 56428ec28bd99f57a3b3422c35ce1110
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
# 查询Linux Servers组的信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 # "Zabbix servers",
#                 "Linux servers"  # 'groupid': '2'
#             ]
#         }
#     },
#     "auth": "56428ec28bd99f57a3b3422c35ce1110",
#     "id": 1
# }
###################################
# 查询Template os linux模板的id
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"  # 'templateid': '10001'
#             ]
#         }
#     },
#     "auth": "56428ec28bd99f57a3b3422c35ce1110",
#     "id": 1
# }
###################################
# 创建名为web1的主机，加入到Linux servers组中，应用Template OS linux模板
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
    "auth": "56428ec28bd99f57a3b3422c35ce1110",
    "id": 1
}

###################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 主要关心result的内容
