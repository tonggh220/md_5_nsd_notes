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