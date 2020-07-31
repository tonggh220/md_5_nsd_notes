# nsd2002-devops-day04

[TOC]

## CI/CD

- CI/CD：持续集成、持续交付

- 程序传统上线流程

```mermaid
graph TD
dev(程序员)--递交-->qs(测试部)
qs--反馈-->dev
dev--提交-->ops(运维部)
```

- 程序语言分类
  - 解释执行：python / shell / php
  - 编译执行：c / c++ / go / java

- CI/CD流程

```mermaid
graph LR
dev(程序员)--提交-->scm(git)
jenkins(jenkins)--克隆-->scm
app1(应用服务器)--下载-->jenkins
app2(应用服务器)--下载-->jenkins
app3(应用服务器)--下载-->jenkins
app4(应用服务器)--下载-->jenkins
```

## git应用

- 安装与配置

```shell
[root@dev ~]# yum install -y git
[root@dev ~]# git config --global user.name zhangzhg
[root@dev ~]# git config --global user.email zhangzg@tedu.cn
[root@dev ~]# git config --global core.editor vim
[root@dev ~]# git config --list
user.name=zhangzhg
user.email=zhangzg@tedu.cn
core.editor=vim
```



