import requests
import json

url = '您机器人的webhook地址'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {
    "msgtype": "text",   # 消息类型为决普通文本
    "text": {
        "content": "好好学习天天向上，我就是我, 是不一样的烟火@156xxxx8827"
    },
    "at": {  # @哪些人
        "atMobiles": [
            # "156xxxx8827",
            # "189xxxx8325"
        ],
        "isAtAll": False  # 要不要@所有人
    }
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
