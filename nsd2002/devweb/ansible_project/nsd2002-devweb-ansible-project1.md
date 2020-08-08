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

