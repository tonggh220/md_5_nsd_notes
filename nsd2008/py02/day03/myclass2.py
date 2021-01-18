class Role:
    def __init__(self, name, mp, hp, weapon):
        # 被称作构造器方法，实例化时自动调用。self不是关键字
        # 用任意名称都可以，当创建时例时，用于将属性绑定到实例身上
        self.name = name
        self.mp = mp
        self.hp = hp
        self.weapon = weapon

class Weapon:
    def __init__(self, wname, strength, type):
        self.wname = wname
        self.strength = strength
        self.type = type

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100, '物理伤害')
    print(ji.wname, ji.strength, ji.type)
    lb = Role('吕布', 300, 500, ji)
    print(lb.weapon.wname, lb.weapon.strength, lb.weapon.type)
