# nsd2002-devops-day01

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

