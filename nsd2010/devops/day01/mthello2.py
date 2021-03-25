import threading

def hello(word):
    print(f'Hello {word}!')

if __name__ == '__main__':
    for w in ['world', 'china', 'tedu']:
        t = threading.Thread(target=hello, args=(w,))  # 创建工作线程
        t.start()  # 启动线程，相当于调用target(*args)
