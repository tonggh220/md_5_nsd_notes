import threading
import time

def hello(word):
    time.sleep(2)
    print('Hello %s!' % word)

if __name__ == '__main__':
    for w in ['World', 'China', 'Tedu']:
        t = threading.Thread(target=hello, args=(w,))  # 创建工作线程
        t.start()   # 启动工作线程，相当于调用target(*args)
