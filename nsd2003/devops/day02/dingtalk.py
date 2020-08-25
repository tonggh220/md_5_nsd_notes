import requests
import json

url = ''
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "好好学习天天向上 我就是我, 是不一样的烟火@156xxxx8827"
#     },
#     "at": {  # @xxxxx
#         "atMobiles": [
#
#         ],
#         "isAtAll": False   # 是否@所有人
#     }
# }

data = {
     "msgtype": "markdown",
     "markdown": {
         "title": "七夕节",
         "text": "#### 七夕节\n> 银烛秋光冷画屏，轻罗小扇扑流萤。天街夜色凉如水，卧看牵牛织女星。\n好好学习天天向上 \n> ![screenshot](https://pic.baike.soso.com/ugc/baikepic2/0/ori-20190731102011-1567992092_jpg_686_516_44418.jpg/800)\n> ###### 七夕 [七夕](https://baike.sogou.com/v179909070.htm) \n"
     },
      "at": {
          "atMobiles": [
          ],
          "isAtAll": False
      }
 }

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
