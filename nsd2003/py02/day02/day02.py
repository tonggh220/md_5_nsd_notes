def func1():
    print('fn 1')
    func2()

def func2():
    print('fn 2')

if __name__ == '__main__':
    func1()
