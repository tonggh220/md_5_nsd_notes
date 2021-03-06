# nsd2002-devops-day02

[TOC]

## paramiko模块

- 它实现了ssh客户端的功能，也可以实现sftp功能

```python
# 安装
[root@localhost day02]# pip3 install paramiko
>>> import paramiko
>>> ssh = paramiko.SSHClient()
# 设置自动接受服务器的主机密钥
>>> ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 登陆
>>> ssh.connect('192.168.1.136', username='root', password='redhat', port=22)
# 执行命令
>>> result = ssh.exec_command('id root; id zhangsan')
>>> len(result)
3
# 执行命令的返回值是一个长度为3的元组。这三项分别是输入、输出和错误的类文件对象
>>> stdin, stdout, stderr = ssh.exec_command('id root; id zhangsan')
>>> out = stdout.read()
>>> err = stderr.read()
>>> out
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> err
b'id: zhangsan: no such user\n'
>>> out.decode()  # bytes转str
'uid=0(root) gid=0(root) 组=0(root)\n'
>>> err.decode()
'id: zhangsan: no such user\n'
# 关闭连接
>>> ssh.close()
```

## 邮件编程

- 准备邮件：使用email模块
- 发送邮件：使用smtplib模块

## JSON

- JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式
- 基于JavaScript Programming Language
- JSON采用完全独立于语言的文本格式
- 这些特性使JSON成为理想的数据交换语言

```python
>>> import json
>>> d1 = {'name': 'tom', 'age': 20}  # 创建字典
>>> json.dumps(d1)  # 将字典转成json字符串
'{"name": "tom", "age": 20}'
>>> jdata = json.dumps(d1)  # 将json字符串转换回字典
>>> json.loads(jdata)
{'name': 'tom', 'age': 20}
>>> data = json.loads(jdata)
>>> data['age']
20
```

- api：Application Programming Interface应用程序编程接口。编程接口就是服务器上对外开放的一个函数，通常以http协议开放。
- 例，中国天气网查询天气情况的api：http://www.weather.com.cn/data/sk/城市代码.html

## requests模块

- http方法。通过http协议访问服务器时，一定是通过某种方法访问。
  - GET：get方法请求指定的页面信息，返回实体主体。该请求是向服务器请求信息，请求参数会跟在url后面，因此，对传参长度有限制的，而且不同浏览器的上限是不同的（2k, 7~8k及其他）。由于get请求直接将参数暴露在url中，因此对于一些带有重要信息的请求可能并不完全合适。比如在浏览器的地址栏中输入网址、比如点击页面上的超链接、比如搜索表单提交，都是get。
  - POST：post请求是向指定资源提交数据进行处理请求，例如提交表单或者上传文件等。数据被包含在请求体中，POST请求可能会导致新的资源的建立和/或已有资源的修改。post方法没有对传递资源的大小进行限制，往往是取决于服务器端的接受能力，而且，该方法传参安全性稍高些


- requests模块将每种http方法都封装成了一个函数，需要使用哪一种方法访问服务器，只要调用同名函数即可。
- 是用Python语言编写的、优雅而简单的HTTP库
- requests内部采用来urillib3

```python
[root@localhost day02]# pip3 install requests
>>> import requests
# 1. 获取文本内容
>>> url1 = 'http://www.163.com'
>>> r = requests.get(url1)
>>> r.text
# 2. 获取非文本内容
>>> url2 = 'http://pic1.win4000.com/wallpaper/a/584ba8f522661.jpg'
>>> r = requests.get(url2)
>>> with open('/tmp/girl.jpg', 'wb') as fobj:
...   fobj.write(r.content)
# 3. 获取json串（序列化数据）
>>> url3 = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> r = requests.get(url3)
>>> r.json()
{'weatherinfo': {'city': 'å\x8c\x97äº¬', 'cityid': '101010100', 'temp': '27.9', 'WD': 'å\x8d\x97é£\x8e', 'WS': 'å°\x8fäº\x8e3çº§', 'SD': '28%', 'AP': '1002hPa', 'njd': 'æ\x9a\x82æ\x97\xa0å®\x9eå\x86µ', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
>>> r.encoding  # 查看当前编码
'ISO-8859-1'
>>> r.encoding = 'utf8'  # 修改编码
>>> r.json()  # 获取json串转成的对象
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9', 'WD': '南风', 'WS': '小于3级' '28%', 'AP': '1002hPa', 'njd': '暂无实况', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1'adar': 'JC_RADAR_AZ9010_JB'}}
```

- requests.get方法传参，使用params完成。
- requests相关方法通过headers传递请求头
- request.post发送数据时，使用data完成

### 使用阿里云开发者平台

- http://www.aliyun.com -> 云市场 -> api市场
- 查天气：搜索天气，找到“杭州网尚科技” -> 0元购买 -> 管理控制台

### 使用钉钉机器人

- https://www.jianshu.com/p/a3c62eb71ae3
- https://im.dingtalk.com/  web登陆地址
- https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq ： 机器人使用说明

- 群 -> 点击机器人图标，创建一个webhook机器人

### 图灵机器人

- https://www.jianshu.com/p/3c0436af6e92
- 微信模块：itchat

### zabbix

- https://www.zabbix.com/documentation/3.4/zh/manual