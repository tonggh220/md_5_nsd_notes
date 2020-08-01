# nsd2002-devops-day05

[TOC]

## jenkins

```mermaid
graph LR
dev(程序员)--提交-->scm(git)
jenkins(jenkins)--克隆-->scm
app1(应用服务器)--下载-->jenkins
app2(应用服务器)--下载-->jenkins
app3(应用服务器)--下载-->jenkins
app4(应用服务器)--下载-->jenkins
```

- Jenkins是由java编写的一款开源软件
- 作为一款非常流行的CI（持续集成）工具，用于构建和测试各种项目
- Jenkins 的主要功能是监视重复工作的执行，例如软件工程的构建或在cron下设置的jobs 

- 持续集成（CI）是当下最为流行的应用程序开发实践方式
- 程序员在代码仓库中集成了修复bug、新特性开发或是功能革新
- CI工具通过自动构建和自动测试来验证结果。这可以检测到当前程序代码的问题，迅速提供反馈

- 安装

```shell
[root@jenkins ~]# rpm -qa | grep java
java-1.8.0-openjdk-1.8.0.161-2.b14.el7.x86_64
[root@jenkins ~]# rpm -ihv jenkins-2.235.3-1.1.noarch.rpm 
[root@jenkins ~]# systemctl start jenkins
[root@jenkins ~]# systemctl enable jenkins
# 访问 http://x.x.x.x:8080
```





























