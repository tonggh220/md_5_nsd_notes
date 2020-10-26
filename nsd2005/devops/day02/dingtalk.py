import requests
import json

url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "好好学习天天向上, 我就是我, 是不一样的烟火@156xxxx8827"
#     },
#     "at": {
#         "atMobiles": [
#             # "156xxxx8827",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False  # 是否@所有人
#     }
# }
data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "重阳节",
        "text": """#### 九月九日忆山东兄弟
独自异乡为异客，每逢佳节倍思亲。遥知兄弟登高处，便插茱萸少一人。
![](http://pic43.photophoto.cn/20170410/0020033007367731_b.jpg)
[好好学习天天向上](http://www.tmooc.cn)"""
    },
    "at": {
        "atMobiles": [
            "150XXXXXXXX"
        ],
        "isAtAll": False
    }
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
