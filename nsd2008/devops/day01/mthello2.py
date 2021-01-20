import threading
import time

def hello(word):
    time.sleep(3)
    print('Hello %s!' % word)

if __name__ == '__main__':
    for i in ['China', 'World', 'Tedu']:
        t = threading.Thread(target=hello, args=(i,))
        t.start()  # 启动工作线程，相当于调用target(*args)
