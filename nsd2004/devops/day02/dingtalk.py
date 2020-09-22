import requests
import json

# 此url就是你的机器人的webhook地址
url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "我就是我, 是不一样的烟火@156xxxx8827 好好学习天天向上"
#     },
#     "at": {
#         "atMobiles": [
#             # "156xxxx8827",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False   # @所有人
#     }
# }
data = {
     "msgtype": "markdown",
     "markdown": {
         "title": "中秋节",
         "text": """## 中秋节放假通知
![](http://s02.ourgame.com.cn/g1/M00/38/C5/wKgCyVYHhiWiceSsAAGPsQ7pkzM590.jpg)
好好学习天天向上 [TMOOC](http://www.tmooc.cn)
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
