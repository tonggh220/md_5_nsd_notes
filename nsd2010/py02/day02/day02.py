def func1():
    print('from func1')
    func2()

def func2():
    print('from fn2')

if __name__ == '__main__':
    func1()
