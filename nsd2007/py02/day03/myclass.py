class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        # 被称作构造器方法，实例化时自动调用。self不是关键字，用任意名称都可以
        # 当创建时例时，用于将属性绑定到实例身上
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

    def show_me(self):
        # 绑定在实例身上的方法，在类中任意位置可见可用
        print('我是%s，擅用%s' % (self.name, self.weapon))

if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')  # 自动调用__init__
    lb.show_me()
