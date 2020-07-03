import requests
import getpass
import json

# url复制粘贴你的webhook
url = getpass.getpass()
headers = {'Content-Type': 'application/json;charset=utf-8'}
# get方法使用params传参数，post方法常用data发送数据
# data数据来自于开发者手册说明
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "好好学习天天向上。我就是我, 是不一样的烟火@156xxxx8827"
#     },
#     "at": {  # at哪些人
#         "atMobiles": [
#             # "156xxxx8827",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False  # 是否at所有人
#     }
# }

data = {
    "msgtype": "markdown",
    "markdown": {
         "title": "六一儿童节放假通知",
         "text": """#### 六一儿童节放假通知, 好好学习天天向上
> ![childrenday](https://my.yjbys.com/uploads/image/20160521/1463802462139521.jpg)
> ##### 10点20分发布 [六一儿童节放假通知](http://www.nipic.com/show/17281068.html)
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
