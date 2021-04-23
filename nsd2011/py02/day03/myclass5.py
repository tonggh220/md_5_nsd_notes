class A:
    def func1(self):
        print('A func')

class B:
    def func2(self):
        print('B func')

class C(A, B):
    def func3(self):
        print('C func')

if __name__ == '__main__':
    c1 = C()
    c1.func1()
    c1.func2()
    c1.func3()
