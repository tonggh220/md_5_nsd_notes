import time
import threading

def hello(word):
    time.sleep(3)
    print('Hello %s!' % word)

if __name__ == '__main__':
    for i in ['world', 'china', 'tedu']:
        # hello(i)
        t = threading.Thread(target=hello, args=(i,))  # 创建工作线程
        t.start()  # 启动工作线程，相当于调用target(*args)
