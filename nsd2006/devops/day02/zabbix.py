import requests
import json

url = 'http://192.168.1.11/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
###################################
# 公开数据可以直接查询
data = {
    "jsonrpc": "2.0",  # 固定内容
    "method": "apiinfo.version",
    "params": [],
    "id": 101  # 随便指定一个数字，表示作业ID
}


###################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 主要关心result的内容

