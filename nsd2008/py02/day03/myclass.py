class Role:
    def __init__(self, name, mp, hp, weapon):
        # 被称作构造器方法，实例化时自动调用。self不是关键字
        # 用任意名称都可以，当创建时例时，用于将属性绑定到实例身上
        self.name = name
        self.mp = mp
        self.hp = hp
        self.weapon = weapon

    def show_me(self):
        # 绑定在实例身上的方法，在类中任意位置可见可用
        print("我是%s，擅用%s" % (self.name, self.weapon))

    def speak(self, words):
        # 没有绑在实例身上的变量，只是函数的局部变量，只能用在当前函数中
        hh = '呵呵'
        print(hh, words)

if __name__ == '__main__':
    # 自动调用__init__，创建具体的实例对象
    lb = Role('吕布', 300, 500, '方天画戟')
    print(lb.name, lb.weapon, lb.mp, lb.hp)
    lb.show_me()
    lb.speak('马中赤兔，人中吕布！')
    zf = Role('张飞', 300, 500, '丈八蛇矛')
    zf.show_me()
    zf.speak('吾乃燕人张飞张冀德')
