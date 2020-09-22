import requests
import json

# 此url就是你的机器人的webhook地址
url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {
    "msgtype": "text",
    "text": {
        "content": "我就是我, 是不一样的烟火@156xxxx8827 好好学习天天向上"
    },
    "at": {
        "atMobiles": [
            # "156xxxx8827",
            # "189xxxx8325"
        ],
        "isAtAll": False   # @所有人
    }
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
