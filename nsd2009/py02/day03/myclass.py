class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        """被称作构造器方法，实例化时自动调用。
        self不是关键字，用任意名称都可以
        当创建时例时，用于将属性绑定到实例身上
        """
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

    def show_me(self):
        # 绑定在实例身上的属性，在类中任意位置可见可用
        print('我是%s，擅用%s' % (self.name, self.weapon))

    def speak(self, words):
        # 没有绑在实例身上的变量，只是函数的局部变量，只能用在当前函数中
        hh = '呵呵'
        print(hh)
        print(words)

if __name__ == '__main__':
    # 实例本身将会自动作为第一个参数传递，本例中是lb
    lb = Role('吕布', '方天画戟')  # 自动调用__init__，创建具体的实例对象
    print(lb.name, lb.weapon, lb.hp, lb.mp)
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')
