# nsd2002-devweb-ansible-project1

## 启动前一个班的项目

### 虚拟环境

- 可以简单的理解为虚拟环境就是一个隔离的运行目录
- 通过venv模块创建一个目录，将python放到这个目录中，就实现了一个虚拟环境
- 安装软件包时，可以安装在虚拟环境下
- 如果不再需要虚拟环境了，直接删除目录即可
- 配置虚拟环境

```shell
# 新建虚拟环境
[root@localhost ~]# python3 -m venv dj1env
[root@localhost ~]# ls -d dj1env
dj1env

# 激活虚拟环境
[root@localhost ~]# source dj1env/bin/activate
(dj1env) [root@localhost ~]# 
(dj1env) [root@localhost ~]# python --version
Python 3.6.8   # 虚拟环境中，python就是python3

# 在虚拟环境下安装软件包
(dj1env) [root@localhost ~]# pip install ansible==2.7.17 ansible-cmdb sqlalchemy django==1.11.6
```

### 启动前一个班的项目

```shell
(dj1env) [root@localhost ~]# cp -r nsd2020/nsd1912/devweb/ansible_project/myansible/ /tmp
(dj1env) [root@localhost ~]# cd /tmp/myansible/
(dj1env) [root@localhost myansible]# python manage.py runserver
```

## 项目：web化运维

### 项目规划

- web采用django2.2.12
- 自动化运维采用ansible2.7.17
- 功能：
  - http://127.0.0.1:8000/：首页，展示所有功能
  - http://127.0.0.1:8000/webadmin/：展示被管理的主机信息
  - http://127.0.0.1:8000/webadmin/add_hosts/：展示、添加主机/主机组
  - http://127.0.0.1:8000/webadmin/add_modules/：展示、添加模块/参数
  - http://127.0.0.1:8000/webadmin/tasks/：用于在特定的主机/主机组执行管理任务

### 项目初始化

- 通过pycharm新建一个名为myansible的django项目

```shell
[root@localhost myansible]# mysql -uroot -ptedu.cn
MariaDB [(none)]> CREATE DATABASE myansible DEFAULT CHARSET utf8mb4;
# myansible/settings.py
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myansible',
        'USER': 'root',
        'PASSWORD': 'tedu.cn',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
```

- 项目包含两个应用：index / webadmin

```shell
[root@localhost myansible]# python3 manage.py startapp index
[root@localhost myansible]# python3 manage.py startapp webadmin
# myansible/settings.py
INSTALLED_APPS = [
    ... ...
    'index',
    'webadmin',
]
```

## 首页应用

### 准备所需材料

```shell
# 拷贝静态文件到项目的根目录下
[root@localhost myansible]# cp -r ../../day02/static/ .
# 声明静态文件位置
# myansible/settings.py  尾部追加
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

### 编写首页应用

```python
# 授权，应用的urls交给应用处理
# myansible/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
]

# vim index/urls.py
from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
]

# index/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')

# mkdir templates/index
# vim templates/index/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ansible Webadmin</title>
</head>
<body>
Ansible Webadmin
</body>
</html>

# 启动开发服务器，监听在0.0.0.0:9000端口
[root@localhost myansible]# python3 manage.py runserver 0:9000

# 使用模板继承，模板采用投票应用的basic.html
[root@localhost myansible]# cp ../../day0304/mysite/templates/basic.html templates/
# templates/index/index.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}Ansible Webadmin{% endblock %}
{% block content %}
    <div class="col-md-3 text-center h4">
        <a href="#" target="_blank">
            <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
            主机信息
        </a>
    </div>
    <div class="col-md-3 text-center h4">
        <a href="#" target="_blank">
            <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
            添加主机
        </a>
    </div>
    <div class="col-md-3 text-center h4">
        <a href="#" target="_blank">
            <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
            添加模块
        </a>
    </div>
    <div class="col-md-3 text-center h4">
        <a href="#" target="_blank">
            <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
            执行任务
        </a>
    </div>
{% endblock %}
```

## webadmin应用

### 数据库模型

```python
# webadmin/models.py
from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ip_addr = models.CharField(max_length=11)
    group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s[%s]" % (self.group, self.hostname, self.ip_addr)

class Module(models.Model):
    modulename = models.CharField(max_length=50)

    def __str__(self):
        return self.modulename

class Argument(models.Model):
    arg_text = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.module, self.arg_text)


# 生成数据库中的表
[root@localhost myansible]# python3 manage.py makemigrations
[root@localhost myansible]# python3 manage.py migrate

# 创建管理员用户
[root@localhost myansible]# python3 manage.py createsuperuser
用户名 (leave blank to use 'root'): admin
电子邮件地址: admin@tedu.cn
Password: 1234.com
Password (again): 1234.com

# 把模型注册到管理后台
# webadmin/admin.py
from django.contrib import admin
from webadmin.models import HostGroup, Host, Module, Argument

for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)
# 登陆到后台http://127.0.0.1:9000/admin添加几个主机和组
```

### 配置ansible工作环境

```shell
[root@localhost myansible]# mkdir ansi_cfg
[root@localhost myansible]# cd ansi_cfg/
[root@localhost ansi_cfg]# vim ansible.cfg
[defaults]
inventory = dhosts.py   # 使用动态主机清单
remote_user = root
[root@localhost ansi_cfg]# touch dhosts.py
[root@localhost ansi_cfg]# chmod +x dhosts.py
```

#### 动态主机清单

- 通过python程序在数据库中取出主机和组，输出格式要求如下：

```json
{
    "组1": {
        "hosts": ["主机1", "主机2"]
    },
    "组2": {
        "hosts": ["主机1", "主机2"]
    }
}
```

- 代码实现

```python
[root@localhost ansi_cfg]# vim dhosts.py
#!/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/myansible?charset=utf8',
     encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50))

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ip_addr = Column(String(11))
    group_id = Column(Integer, ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.groupname, Host.ip_addr).join(Host)
    # print(qset.all())
    result = {}
    for g, ip in qset:
        if g not in result:  # 组不在字典中，新建项目
            result[g] = {}
            result[g]['hosts'] = []
        result[g]['hosts'].append(ip)  # 把ip地址追加到列中
    print(result)
    
[root@localhost ansi_cfg]# ansible all -m ping
```

### 实现主机信息页

```python
# 授权，webadmin的url交给webadmin应用处理
# myansible/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webadmin/', include('webadmin.urls')),
    path('', include('index.urls')),
]

# webadmin/urls.py
from django.urls import path
from webadmin import views

urlpatterns = [
    path('', views.index, name='webadin_index'),
]

# mkdir templates/webadin
# webadmin/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'webadmin/index.html')

# 通过ansible-cmdb生成主机信息页
[root@localhost ansi_cfg]# ansible dbservers -m setup --tree /tmp/myhosts
[root@localhost ansi_cfg]# ansible-cmdb /tmp/myhosts > ../templates/webadmin/index.html

# 修改templates/index/index.html中主机信息的超链接
<a href="{% url 'webadin_index' %}" target="_blank">
    <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
    主机信息
</a>
```



