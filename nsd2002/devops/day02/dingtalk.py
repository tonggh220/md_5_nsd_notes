import requests
import json

url = '您机器人webhook地址'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "msgtype": "text",   # 消息类型为决普通文本
#     "text": {
#         "content": "好好学习天天向上，我就是我, 是不一样的烟火@156xxxx8827"
#     },
#     "at": {  # @哪些人
#         "atMobiles": [
#             # "156xxxx8827",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False  # 要不要@所有人
#     }
# }
data = {
     "msgtype": "markdown",
     "markdown": {
         "title": "中秋节放假通知",
         "text": """##中秋节放假通知
好好学习天天向上。[中秋节放假通知](http://www.tmooc.cn)
![](http://pic141.nipic.com/file/20170927/13663111_095949886000_2.jpg)
"""
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
