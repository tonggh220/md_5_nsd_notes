# nsd2004-devops-day01

## 多进程

- os.fork()产生子进程
- os.fork()的返回值是数字，在父子进程中不一样。在子进程中是0，父进程是非0值（子进程的PID）

```python
import os

print('starting...')
ret_val = os.fork()
if ret_val:  # 如果是父进程，值非0，为真；如果是子进程，值是0，为假
    print('parent')
else:
    print('child')

print('Hello World!')
```

- 父子是相对的，子进程还可以再生成子进程
- 多进程编程思路
  - 父进程只产生子进程
  - 子进程做具体的工作
  - 子进程做完工作后，需要通过exit彻底结束

```python
import os

for i in range(3):
    ret_val = os.fork()
    if not ret_val:
        print('Hello World!')
        exit(0)
```

### 僵尸进程

- 当子进程结束后，它没有任何可执行代码时，就成为了僵尸进程。
- 短暂存在的程序，不用考虑僵尸进程问题。因为systemd会处理。

## 多线程编程

- 程序是存储在磁盘上的可执行文件
- 运行程序后，将会生成一或多个进程。所以可以认为进程是程序的一次执行，是加载到内存中的一系列指令。
- 每个进程都拥有它自己的运行空间。
- 一个进程可以产一到多个线程，线程是CPU的最小调度单位。
- 多个线程共享进程的运行空间。
- linux系统支持多进程和多线程。
- windows系统不支持多进程。
- 多线程编程思路
  - 主线程产生工作线程
  - 工作线程做具体的工作

```python
import threading

def hello():
    print('Hello World!')

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=hello)  # 创建工作线程
        t.start()  # 启动工作线程，相当于执行target()
```

## urllib模块

- 用于访问网络资源

```python
>>> from urllib import request
>>> url = 'http://www.163.com'
>>> html = request.urlopen(url)
>>> html.readline()
b' <!DOCTYPE HTML>\n'
>>> html.read(10)
b'<!--[if IE'
>>> html.readlines()
```

#### wget模块

- wget模块对urllib模块进行封装，可以方便地实现下载功能

```python
# 安装
[root@localhost day01]# pip3 install wget
>>> import wget
>>> url = 'http://n.sinaimg.cn/ent/4_img/upload/eca303e9/125/w690h1035/20200724/2843-iwtqvyk9763395.jpg'
>>> wget.download(url, '/tmp/g.jpg')
```

#### 修改请求头

```python
>>> url = 'https://www.jianshu.com/'
>>> html = request.urlopen(url)
... ...
urllib.error.HTTPError: HTTP Error 403: Forbidden
# 服务器大多都有反爬虫设置，如果发现客户端是爬虫，可能拒绝访问
# 修改请求头，将User-Agent改为正常的浏览器
>>> headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
# 创建请求对象
>>> r = request.Request(url, headers=headers)
>>> html = request.urlopen(r)  # 携带修改的请求头访问url
>>> html.read()
```

#### 数据编码

- 一般来说，URL标准中只会允许一部分ASCII字符，比如数字、字母、部分符号等
- 其他字符需要编码

```python
>>> url = 'https://www.sogou.com/web?query=端午节'
>>> html = request.urlopen(url)  # 报错
>>> url = 'https://www.sogou.com/web?query=' + request.quote('中秋节')
>>> url
'https://www.sogou.com/web?query=%E4%B8%AD%E7%A7%8B%E8%8A%82'
```

#### 异常处理

- urllib的异常保存在urllib.error模块中，捕获异常时，需导入它

```python
[root@localhost ~]# mkdir -m 000 /var/www/html/ban
>>> url1 = 'http://127.0.0.1/ban'  # 没权限
>>> url2 = 'http://127.0.0.1/abc'  # 没有该路径
>>> request.urlopen(url1)
urllib.error.HTTPError: HTTP Error 403: Forbidden
>>> request.urlopen(url2)
urllib.error.HTTPError: HTTP Error 404: Not Found
>>> from urllib import error
>>> try:
...   request.urlopen(url1)
... except error.HTTPError as e:
...   print('Error:', e)
... 
Error: HTTP Error 403: Forbidden
```

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
