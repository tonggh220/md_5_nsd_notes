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

