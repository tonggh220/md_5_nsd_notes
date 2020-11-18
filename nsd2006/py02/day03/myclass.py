class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何合法变量名
        # 绑定在实身上的属性，可以在类中任意位置使用
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s，擅用%s' % (self.name, self.weapon))

    def speak(self, words):
        # 没有绑在实例身上的变量，就是局部变量，只能在函数中使用
        hh = 'Hahahahahaha'
        print(hh)
        print(words)

if __name__ == '__main__':
    # 创建实例时，如果类中有__init__方法，自动调用它，实例本身自动成为第一个参数
    lb = Role('吕布', '方天画戟')  # 实例化，通过类创建具体的实例对象
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')
