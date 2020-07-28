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











