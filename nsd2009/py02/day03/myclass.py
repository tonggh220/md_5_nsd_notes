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

if __name__ == '__main__':
    # 实例本身将会自动作为第一个参数传递，本例中是lb
    lb = Role('吕布', '方天画戟')  # 自动调用__init__，创建具体的实例对象
    print(lb.name, lb.weapon, lb.hp, lb.mp)

