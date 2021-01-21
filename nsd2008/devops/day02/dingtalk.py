import requests
import json

url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {
    "msgtype": "text",
    "text": {
        "content": "好好学习天天向上我就是我, 是不一样的烟火@156xxxx8827"
    },
    "at": {
        "atMobiles": [  # @哪些人
            # "156xxxx8827",
            # "189xxxx8325"
        ],
        "isAtAll": False  # @所有人
    }
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
