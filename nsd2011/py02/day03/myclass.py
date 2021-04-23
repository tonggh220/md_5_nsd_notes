class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        # 被称作构造器方法，实例化时自动调用
        # self不是关键字，可以是自定义的任何名字，表示实例本身
        # 当创建实例时，用于将属性绑定到实例身上
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')  # 自动调用__init__，创建具体的实例对象
    print(lb.name, lb.weapon, lb.hp, lb.mp)
