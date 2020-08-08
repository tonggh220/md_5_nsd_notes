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







