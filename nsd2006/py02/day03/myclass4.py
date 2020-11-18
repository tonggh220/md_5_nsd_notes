class Role:
    def __init__(self, name, weapon, mp, hp):
        self.name = name
        self.weapon = weapon
        self.mp = mp
        self.hp = hp

class Warrior(Role):
    def __init__(self, name, weapon, mp, hp, country):
        # Role.__init__(self, name, weapon, mp, hp)
        super(Warrior, self).__init__(name, weapon, mp, hp)
        self.country = country

    def attack(self, target):
        print('与%s近身肉搏' % target)

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟', 500, 1000, '东汉')
    print(lb.country)
