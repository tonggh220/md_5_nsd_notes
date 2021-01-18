class A:
    def func1(self):
        print('A func')

    def func4(self):
        print('aaaa fun4')

class B:
    def func2(self):
        print('B func')

    def func4(self):
        print('bbbb fn4')

class C(B, A):
    def func3(self):
        print('C func')

    def func4(self):
        print('cccc fn4')

if __name__ == '__main__':
    c1 = C()
    # c1.func1()
    # c1.func2()
    # c1.func3()
    c1.func4()
