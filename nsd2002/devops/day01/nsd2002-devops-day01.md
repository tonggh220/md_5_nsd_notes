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

