import requests
import json

url = '机器人webhook地址'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "我就是我, @150XXXXXXXX 是不一样的烟火 好好学习天天向上"
#     },
#     "at": {
#         "atMobiles": [   # @手机号
#             # "150XXXXXXXX"
#         ],
#         "isAtAll": False  # 是否@所有人
#     }
# }
data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"清明节放假通知",
         "text": '''## 清明节放假通知
4月3日至4月5日放假3天
![](http://img0.pconline.com.cn/pconline/1504/03/6294556_apic101491_thumb.jpg)
好好学习天天向上 [TMOOC](http://tmooc.cn)
'''
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
