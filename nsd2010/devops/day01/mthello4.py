import threading

class Hello:
    def __init__(self, word):
        self.word = word

    def __call__(self):
        print(f'Hello {self.word}!')

if __name__ == '__main__':
    for w in ['world', 'china', 'tedu']:
        t = threading.Thread(target=Hello(w))  # 创建工作线程
        t.start()  # 启动线程，相当于调用target()
