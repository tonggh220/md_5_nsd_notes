class Role:
    def __init__(self, name, hp, mp, weapon):
        # 被称作构造器方法，实例化时自动调用。self不是关键字，用任意名称都可以
        # 当创建时例时，用于将属性绑定到实例身上
        self.name = name
        self.hp = hp
        self.mp = mp
        self.weapon = weapon

if __name__ == '__main__':
    lb = Role('吕布', 500, 200, '方天画戟')  # 自动调用__init__，创建具体的实例对象
    print(lb.name, lb.mp, lb.hp, lb.weapon)
    zf = Role('张飞', 500, 200, '丈八蛇矛')
    print(zf.name, zf.mp, zf.hp, zf.weapon)
