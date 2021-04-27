import requests
import json

url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {
    "at": {
        "atMobiles ": [   # @手机号
            # "180xxxxxx"
        ],
        "atUserIds ": [   # @用户
            # "user123"
        ],
        "isAtAll ": False   # 是否 @所有人
    },
    "text": {
        "content": "我就是我, @XXX 是不一样的烟火 好好学习天天向上"
    },
    "msgtype": "text"
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
