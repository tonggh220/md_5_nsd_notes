# nsd1912-devops-day02

## 邮件

- SMTP：简单邮件传输协议，TCP25端口。主要用于发送邮件。
- 发邮件编程，主要在于两点：
  - 准备邮件：使用email模块
  - 发送邮件：使用smtplib模块

# JSON

- JavaScript Object Notation。是一种轻量级的数据交换格式
- API：应用程序编程接口。访问API时，将会调用它的相关函数
- 不同的编程语言，它们的数据类型不一样
- 服务器和客户端通过程序通信时，不需要使用完全一样的编程语言。
- JSON采用完全独立于语言的文本格式。
- 语言之间传送数据时，一端将数据转成JSON字符串发送，另一端接收时再将JSON字符串转换成它可以理解的数据类型。

```python
>>> import json
# 发送端，将字典转成json字符串
>>> d1 = {'name': 'bob', 'age': 20}
>>> json.dumps(d1)
'{"name": "bob", "age": 20}'
>>> data = json.dumps(d1)
>>> type(data)
<class 'str'>

# 接收端，将收到的json字符串还原成字典。
>>> json.loads(data)
{'name': 'bob', 'age': 20}
>>> jdata = json.loads(data)
>>> type(jdata)
<class 'dict'>

# 将字典转成json字符串写入文件
>>> with open('/tmp/j.dta', 'w') as fobj:
...   json.dump(d1, fobj)

# 将json字符串从文件中取出，并还原成字典
>>> with open('/tmp/j.dta') as fobj:
...   d2 = json.load(fobj)
... 
>>> type(d2)
<class 'dict'>
>>> d2
{'name': 'bob', 'age': 20}
```

## requests模块

- requests是用Python语言编写的、优雅而简单的HTTP库
- requests内部采用urillib3
- requests将常用的http方法都定义好了相关的函数，使用什么样的方法访问网络资源，只要调用相关的函数即可
- HTTP常用方法：
  - get：在浏览器中输入地址访问；网页中点击超链接；搜索表单
  - post：登陆、注册表单

```python
[root@localhost day02]# pip3 install requests
>>> import requests
# 访问文本型的数据
>>> url1 = 'http://www.163.com'
>>> r = requests.get(url1)
>>> r.text

# 访问非文本数据
>>> url2 = 'http://5b0988e595225.cdn.sohucs.com/images/20190602/a584e0bff8d343d189915dade94d89ff.jpeg'
>>> r = requests.get(url2)
>>> r.content
>>> with open('/tmp/61.jpg', 'wb') as fobj:
...   fobj.write(r.content)
[root@localhost day02]# eog /tmp/61.jpg 

# 访问api取得json数据
# 例中国天气网的api：
# http://www.weather.com.cn/data/sk/城市代码.html
# 城市代码自行搜索
>>> url3 = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> r = requests.get(url3)
>>> r.json()  # 乱码
>>> r.encoding  # 查看当前字符编码
'ISO-8859-1'
>>> r.encoding = 'utf8'
>>> r.json()
```

### 使用阿里云的api

https://www.aliyun.com/ -> 登陆后 点击“云市场” -> “API市场”

- 查天气预报：搜索“天气预报” -> 找到“杭州网尚科技”的“全国天气预报查询” -> 点击进入详情页后，点购买 -> 点击“管理控制台” -> 记录自己的appkey / appcode等信息。-> 点击左上角“全国天气预报查询” -> 回到购买页面，它的下面有使用方法

```python
>>> url4 = 'http://jisutianqi.market.alicloudapi.com/weather/query'
>>> params = {'citycode': '101010100'}
>>> headers = {'Authorization': 'APPCODE 369deb7e22c3effbb7e'}
>>> r = requests.get(url4, headers=headers, params=params)
>>> r.json()
>>> import pprint
>>> pprint.pprint(r.json())
>>> data = r.json()
>>> data['result']['daily'][0]['day']['temphigh']
>>> data['result']['daily'][0]['night']['templow']
```

- 老黄历：搜索找到并购买深圳艾科瑞特的老黄历api

```python
>>> url5 = 'http://icalendar.market.alicloudapi.com/ai_metaphysics/calendar/elite'
>>> params = {'STRING': '20200530153000'}
>>> headers = {'Authorization': 'APPCODE 369deb7e22c3effbb7e'}
>>> r = requests.get(url5, params=params, headers=headers)
```

## 使用钉钉机器人

https://www.jianshu.com/p/a3c62eb71ae3

- 添加机器人

https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq

## 图灵机器人

https://www.jianshu.com/p/3c0436af6e92

## 微信

在简书中搜itchat

## zabbix编程

https://www.zabbix.com/documentation/3.4/zh/manual -> api

- zabbix api url：在zabbix web目录下名为`apiinfo.version`
  - http://192.168.81.132/zabbix/api_jsonrpc.php
- 如果访问共公内容，可以直接访问
- 如果访问私有数据，需要认证信息

