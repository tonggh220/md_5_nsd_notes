import requests
import json

url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
########################
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "我就是我, 是不一样的烟火@156xxxx8827好好学习天天向上"
#     },
#     "at": {
#         "atMobiles": [   # @手机号
#             # "156xxxx8827",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False   # @所有人
#     }
# }
########################
data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "元旦放假通知",
        "text": """## 元旦放假通知
![](http://p6.itc.cn/q_70/images03/20201217/9effd2dd87934cfca874eb5e6d488fa4.jpeg)
好好学习天天向上
[TMOOC](http://tmooc.cn)
"""
    },
    "at": {
        "atMobiles": [
            # "150XXXXXXXX"
        ],
        "isAtAll": False
    }
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
