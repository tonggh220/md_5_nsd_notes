import time
import threading

def hello(word):
    time.sleep(3)
    print('Hello %s!' % word)

if __name__ == '__main__':
    for w in ['World', 'China', 'Tedu']:
        t = threading.Thread(target=hello, args=(w,))  # 创建工作线程
        t.start()  # 启动线程，将会调用target(*args)
