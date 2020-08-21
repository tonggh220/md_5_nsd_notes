class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何自定义的变量
        # 绑定在实例身上的属性，在类中任意位置可见可用
        self.name = name
        self.weapon = weapon

    def show_me(self):
        # 绑定在实例身上的属性，在类中任意位置可见可用
        print('我是%s，我擅用%s' % (self.name, self.weapon))

    def speak(self, word):
        # 没有绑定在实例身上的变量，只是局部变量，只能用在函数中
        print(word)

if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')
    print(lb.name, lb.weapon)
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')
    zf = Role('张飞', '丈八蛇矛')
    zf.show_me()
    zf.speak('我乃燕人张飞张冀德')


