class Role:
    def __init__(self, name, hp, mp, weapon):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.weapon = weapon

class Warrior(Role):
    def __init__(self, name, hp, mp, weapon, qq):
        # self.name = name
        # self.hp = hp
        # self.mp = mp
        # self.weapon = weapon
        # 或
        # Role.__init__(self, name, hp, mp, weapon)
        # 或
        super(Warrior, self).__init__(name, hp, mp, weapon)
        self.qq = qq

if __name__ == '__main__':
    lb = Warrior('吕布', 500, 200, '方天画戟', '23454346')
    print(lb.name, lb.qq)

