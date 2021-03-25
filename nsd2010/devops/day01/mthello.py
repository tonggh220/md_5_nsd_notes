import threading
import time

def hello():
    time.sleep(3)
    print('Hello World!')

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=hello)  # 创建工作线程
        t.start()  # 启动线程，相当于调用target()
        # hello()
