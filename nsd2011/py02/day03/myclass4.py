class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

class Warrior(Role):  # 括号中的Role是父类或基类
    'Role的子类'
    def __init__(self, name, weapon, qq, hp=500, mp=300):
        # self.name = name
        # self.weapon = weapon
        # self.hp = hp
        # self.mp = mp
        # ------------------------------------------
        # Role.__init__(self, name, weapon, hp, mp)
        # ------------------------------------------
        # 上述方法，也可以改为以下表示方式
        super(Warrior, self).__init__(name, weapon, hp, mp)
        self.qq = qq

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟', '234235235')
    print(lb.qq, lb.name)
