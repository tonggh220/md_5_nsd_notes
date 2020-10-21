class A:
    def func1(self):
        print('A func1')

    def func4(self):
        print('aaaaaa func4')

class B:
    def func2(self):
        print('B func2')

    def func4(self):
        print('bbbbb func4')

class C(B, A):
    def func3(self):
        print('C func3')

    def func4(self):
        print('ccccc func4')

if __name__ == '__main__':
    c1 = C()
    c1.func1()
    c1.func2()
    c1.func3()
    c1.func4()
