import requests
import json

url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "好好学习天天向上我就是我, 是不一样的烟火@156xxxx8827"
#     },
#     "at": {
#         "atMobiles": [  # @哪些人
#             # "156xxxx8827",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False  # @所有人
#     }
# }
data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "春节放假通知",
        "text": """## 放假通知
![](http://p6.itc.cn/images01/20210114/b3698b8042d146b1ae167a5fbe3ebf56.jpeg)
好好学习天天向上 [TMOOC](http://tmooc.cn)
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
