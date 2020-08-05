# nsd2002-devweb-day03

## django

### MTV模式

```mermaid
graph LR
c(client)--访问-->s(服务器URLConfig)
s--调用-->v(视图函数Views)
v--crud-->m(模型models)
m--返回-->v
v--加载-->t(网页模板templates)
t--返回-->c
```

### 配置django

```shell
[root@localhost nsd2020]# cat ~/.pip/pip.conf 
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com

# 查看django有哪些版本
[root@localhost nsd2020]# pip3 install django==
[root@localhost nsd2020]# pip3 install django==2.2.12
# 查看安装结果
[root@localhost nsd2020]# python3 -m django --version
2.2.12

# 下载python软件包
[root@localhost pypkgs]# pip3 download django==2.2.12 --trusted-host mirrors.aliyun.com
```

- 创建项目方法一

```shell
[root@localhost day0304]# django-admin startproject mytest
[root@localhost day0304]# ls 
mytest
```

- 创建项目方法二，使用pycharm创建：file -> new project -> 弹出窗口，左侧选django；右侧在Location填入项目目录，最后的目录名为mysite

- 项目目录结构

```shell
[root@localhost mysite]# tree .
.                      # 项目根目录
├── manage.py          # 项目管理文件
├── mysite             # 项目配置目录
│   ├── __init__.py    # 初始化文件
│   ├── settings.py    # 项目配置文件
│   ├── urls.py        # 路由文件
│   └── wsgi.py        # 部署项目到web服务器的配置文件
└── templates          # 存放网页模板的目录
```

- 初始化项目

```python
# 为项目创建数据库
[root@localhost pypkgs]# mysql -uroot -ptedu.cn
MariaDB [(none)]> CREATE DATABASE dj2002 DEFAULT CHARSET utf8;

# 修改项目配置文件
# mysite/settings.py
ALLOWED_HOSTS = ['*']   # 监听在哪些地址上
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj2002',
        'USER': 'root',
        'PASSWORD': 'tedu.cn',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
LANGUAGE_CODE = 'zh-hans'   # 修改语言
TIME_ZONE = 'Asia/Shanghai'

# 启动开发服务器
[root@localhost mysite]# python3 manage.py runserver
# 报错如下：
... ...
Did you install mysqlclient?
# 解决方法
[root@localhost mysite]# yum install -y mariadb-devel
[root@localhost mysite]# pip3 install mysqlclient
# 再次启动开发服务器
[root@localhost mysite]# python3 manage.py runserver
# 访问http://127.0.0.1:8000/
```

- 生成项目默认的数据库

```shell
# 生成数据库
[root@localhost mysite]# python3 manage.py makemigrations
[root@localhost mysite]# python3 manage.py migrate
# 创建管理员用户
[root@localhost mysite]# python3 manage.py createsuperuser
用户名 (leave blank to use 'root'): admin
电子邮件地址: admin@tedu.cn
Password: 1234.com
Password (again): 1234.com
Superuser created successfully.
# 访问管理后台http://127.0.0.1:8000/admin
```

### 配置应用

- 项目由一到多个应用构成
- 每个应用是一个功能模块
- 应用可以集成到多个项目，实现复用

```shell
# 创建投票应用
[root@localhost mysite]# python3 manage.py startapp polls
[root@localhost mysite]# ls
manage.py  mysite  polls  templates
# 集成应用到项目
# mysite/settings.py
INSTALLED_APPS = [
    ... ...
    'polls',
]
```

### 应用规划

- 应用url名称：http://server_ip/app_name/app_url
- 投票应用url规划：
  - http://server_ip/polls：投票首页，用于显示所有投票项
  - http://server_ip/polls/1：1号问题的投票详情页
  - http://server_ip/polls/1/result：1号问题的投票结果页，展示选项所得票数

- 授权，将应用的url交给应用处理

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 从http://server_ip/后面开始匹配
    # 路径是polls/，这种url交给polls应用的urls.py文件处理
    path('polls/', include('polls.urls')),
]

# vim polls/urls.py
from django.urls import path

urlpatterns = []
```

- 制作投票首页：http://server_ip/polls

```python
# 编写url与函数的对应关系
# vim polls/urls.py
from django.urls import path
from polls import views

urlpatterns = [
    # 从http://server_ip/polls/后面进行匹配
    # polls/后面空的，则调用相关函数views.index
    # name='index'是给http://server_ip/polls/起的名字
    path('', views.index, name='index'),
]

# 编写函数
# polls/views.py
from django.shortcuts import render

# 用户发起的请求，请求将会成为一个对象，作为第一个参数传给函数
# 因此，函数至少需要有一个参数
def index(request):
    # index函数通过render函数找到一个网页模板文件，返回给客户端
    return render(request, 'index.html')

# 创建网页模板文件
# vim templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
</head>
<body>
<h1>投票首页</h1>
</body>
</html>

# 测试
[root@localhost mysite]# python3 manage.py runserver
# 访问http://127.0.0.1:8000/报404是正常的
# 访问http://127.0.0.1:8000/polls/
```

- 制作投票详情页

```python
# polls/urls.py
from django.urls import path, re_path
from polls import views

urlpatterns = [
    # 从http://server_ip/polls/后面进行匹配
    # polls/后面空的，则调用相关函数views.index
    # name='index'是给http://server_ip/polls/起的名字
    path('', views.index, name='index'),
    # path()函数中的路径，可以支持变量。声明一个名为qid，类型为int的变量
    # 类型除了int外，还有str和slug
    path('<int:qid>', views.detail, name='detail'),
    # path函数也可以替换为正则表达式，如上面的写法，也可以写为：
    # re_path(r'^(\d+)$', views.detail, name='detail')
]


# polls/views.py
def detail(request, qid):
    # qid用于接收来自于url的参数
    # {'qid': qid}将成为detail.html的变量和值，即 qid=数字
    return render(request, 'detail.html', {'qid': qid})

# templates/detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票详情</title>
</head>
<body>
<h1>{{ qid }}号问题投票详情</h1>
</body>
</html>

# 测试，访问http://server_ip/polls/数字
```

- 制作投票结果页

```python
# polls/urls.py
... ...
    path('<int:qid>/result', views.result, name='result'),
... ...

# polls/views.py
def result(request, qid):
    return render(request, 'result.html', {'qid': qid})

# templates/result.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票结果</title>
</head>
<body>
<h1>{{ qid }}号问题投票结果</h1>
</body>
</html>

# 访问http://server_ip/polls/数字/result
```

## Model模型

- 模型指出了数据的唯一、明确的真实来源
- 它包含了正在存储的数据的基本字段和行为
- Model采用ORM
  - Object
  - Relationship
  - Mapper
  - 数据库的表和python的class映射
  - 表中的字段与class的类变量映射
  - 数据库的数据类型在django中都有提前定义好的，对应的class
  - 表中的记录与class的实例映射
- 每个模型都用一个类表示，该类继承自django.db.models.Model
- 在投票应用中有两个类，分别是Question和Choice

- 创建模型

```python
# polls/models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

# 生成数据库中的表
[root@localhost mysite]# python3 manage.py makemigrations
[root@localhost mysite]# python3 manage.py migrate
# 查看数据库。
# 表名构成：1. 全是小写字母；2. 应用名_类名
MariaDB [dj2002]> show tables;
| polls_question             |
# 分析表结构
# 1. 没有明确声明主键，django自动创建一个名为id的主键
# 2. 类变量成为了字段名
# 3. CharField对应varchar；DateTimeField对应datetie类型
MariaDB [dj2002]> desc polls_question;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | int(11)      | NO   | PRI | NULL    | auto_increment |
| question_text | varchar(200) | NO   |     | NULL    |                |
| pub_date      | datetime(6)  | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

# 创建选项模型
# polls/models.py
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
[root@localhost mysite]# python3 manage.py makemigrations
[root@localhost mysite]# python3 manage.py migrate
# 分析表结构
MariaDB [dj2002]> show tables;
| polls_choice               |
MariaDB [dj2002]> desc polls_choice;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| choice_text | varchar(200) | NO   |     | NULL    |                |
| votes       | int(11)      | NO   |     | NULL    |                |
| q_id        | int(11)      | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
# 注意，在Choice模型中，q是外键，那么在表中字段名是：类变名_id

# 修改外键字段的名字
# polls/models.py
class Choice(models.Model):
    ... ...
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
[root@localhost mysite]# python3 manage.py makemigrations
Did you rename choice.q to choice.question (a ForeignKey)? [y/N] y
[root@localhost mysite]# python3 manage.py migrate
MariaDB [dj2002]> desc polls_choice;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| choice_text | varchar(200) | NO   |     | NULL    |                |
| votes       | int(11)      | NO   |     | NULL    |                |
| question_id | int(11)      | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+

```





```shell

```

