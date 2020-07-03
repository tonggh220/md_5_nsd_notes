import requests
import json

url = 'http://192.168.81.132/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
#################################
# 对于公共数据，可以直接获取
# data = {
#     "jsonrpc": "2.0",  # 协议版本，固定的
#     "method": "apiinfo.version",  # 获取版本信息
#     "params": [],  # 参数
#     "id": 1        # 随便给定一个整数，表示作业id
# }
#################################
# 私有数据需要获取token
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 4d285985bdb0347c0b2896ec765579ec
#################################
# 获取所有主机的信息
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
#     "auth": "4d285985bdb0347c0b2896ec765579ec",
#     "id": 1
# }
# 'hostid': '10084'
#################################
# 删除主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10084",
#     ],
#     "auth": "4d285985bdb0347c0b2896ec765579ec",
#     "id": 1
# }
#################################
# 获取Linux serves组的id
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
#     "auth": "4d285985bdb0347c0b2896ec765579ec",
#     "id": 1
# }
# 'groupid': '2'
#################################
# 获取Template OS linux模板 ID
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
#     "auth": "4d285985bdb0347c0b2896ec765579ec",
#     "id": 1
# }
# 'templateid': '10001'
#################################
# 创建名为web1的主机，属于linus servers组，应用template os linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web1",
        "interfaces": [  # 监控方式
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.81.131",
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
        "inventory_mode": 0,  # 配置主机资产记录
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "4d285985bdb0347c0b2896ec765579ec",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 主要关注result部分
