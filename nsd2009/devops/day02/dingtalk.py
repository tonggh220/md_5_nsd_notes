import requests
import json

url = '你机器人的webhook地址'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {
    "msgtype": "text",
    "text": {
        "content": "我就是我, @150XXXXXXXX 是不一样的烟火 好好学习天天向上"
    },
    "at": {
        "atMobiles": [
            # "150XXXXXXXX"  # @手机号
        ],
        "isAtAll": False  # @是否所有人
    }
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
