import requests
import json

url = 'http://192.168.1.136/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json'}
#######################################
# data = {  # 在手册页上查询得到，查询zabbix版本，不需要认证
#     'jsonrpc': '2.0',
#     'method': 'apiinfo.version',
#     'id': 1,   # 随便给个值，表示作业id
#     'auth': None,
#     'params': {},
# }
############################################
# 获取用户的token
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1,
#     "auth": None
# }
# 获取到的token: 84e1b3eaa1d62ae61cd4937eb0f4f967
############################################
# 查询主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": ["hostid", "host"],
#         "selectInterfaces": [ "interfaceid", "ip" ]
#     },
#     "id": 2,
#     "auth": "84e1b3eaa1d62ae61cd4937eb0f4f967"  # 这里是token
# }
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {  # 过滤满足条件的主机
#             "host": [
#                 # "Zabbix server",
#                 # "Linux server"
#             ]
#         }
#     },
#     "auth": "84e1b3eaa1d62ae61cd4937eb0f4f967",
#     "id": 1
# }
# 获取到主机id: 'hostid': '10084'
############################################
# 获取Linux serves组的id 'groupid': '2'
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
#     "auth": "84e1b3eaa1d62ae61cd4937eb0f4f967",
#     "id": 1
# }
#
############################################
# 获取Template OS linux模板 ID  'templateid': '10001'
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
#     "auth": "84e1b3eaa1d62ae61cd4937eb0f4f967",
#     "id": 1
# }
#
############################################
# 创建名为web1的主机，属于linus servers组，应用template os linux模板
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.create",
#     "params": {
#         "host": "web1",
#         "interfaces": [  # 监控方式
#             {
#                 "type": 1,
#                 "main": 1,
#                 "useip": 1,
#                 "ip": "192.168.1.131",
#                 "dns": "",
#                 "port": "10050"
#             }
#         ],
#         "groups": [
#             {
#                 "groupid": "2"
#             }
#         ],
#         "templates": [
#             {
#                 "templateid": "10001"
#             }
#         ],
#         "inventory_mode": 0,  # 配置主机资产记录
#         "inventory": {
#             "macaddress_a": "01234",
#             "macaddress_b": "56768"
#         }
#     },
#     "auth": "84e1b3eaa1d62ae61cd4937eb0f4f967",
#     "id": 1
# }
############################################
# 删除主机id是'10254'的主机
data = {
    "jsonrpc": "2.0",
    "method": "host.delete",
    "params": [
        "10254",
    ],
    "auth": "84e1b3eaa1d62ae61cd4937eb0f4f967",
    "id": 1
}



############################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 执行的结果，只要关注result

