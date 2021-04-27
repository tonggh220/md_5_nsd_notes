import requests
import json

url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "at": {
#         "atMobiles ": [   # @手机号
#             # "180xxxxxx"
#         ],
#         "atUserIds ": [   # @用户
#             # "user123"
#         ],
#         "isAtAll ": False   # 是否 @所有人
#     },
#     "text": {
#         "content": "我就是我, @XXX 是不一样的烟火 好好学习天天向上"
#     },
#     "msgtype": "text"
# }
data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "放假通知",
        "text": '''## 五一放假通知
5月1日至5日，共放假5天
![](https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2021%2F0421%2Fb0412ef7j00qrw74o004fc000rs00mam.jpg&thumbnail=650x2147483647&quality=80&type=jpg)
好好学习天天向上 [TMOOC](http://tmooc.cn)
'''
    },
    "at": {
        "atMobiles": [
            "150XXXXXXXX"
        ],
        "atUserIds": [
            "user123"
        ],
        "isAtAll": False
    }
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
