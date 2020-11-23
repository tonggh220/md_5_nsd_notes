import requests
import json

url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "我就是我, 是不一样的烟火 好好学习天天向上"
#     },
#     "at": {  # @哪些电话号码
#         "atMobiles": [
#             # "156xxxx8827",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False   # 是否@所有人
#     }
# }

data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "Offer",
        "text": """## 入职邀请
您已被我公司录取，请于2020-12-10来报到，公司详情参见：[TEDU](http://www.tedu.cn)
![](http://cdn.tmooc.cn/bsfile//imgad///17a5069fdce747a6ae107cb6c2db1199.jpg)
好好学习天天向上"""
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
