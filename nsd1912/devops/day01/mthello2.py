import threading

def hello(word):
    print('Hello %s' % word)

if __name__ == '__main__':
    for i in ['World', 'China', 'Tedu']:
        t = threading.Thread(target=hello, args=(i,))  # 创建工作线程
        t.start()  # 启动工作线程，相当地执行target(*args)
