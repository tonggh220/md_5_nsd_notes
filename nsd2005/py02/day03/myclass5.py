class Role:
    def __init__(self, name, weapon, hp, mp):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

class Warrior(Role):
    def __init__(self, name, weapon, hp, mp, ride):
        # Role.__init__(self, name, weapon, hp, mp)
        super(Warrior, self).__init__(name, weapon, hp, mp)
        self.ride = ride

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟', 100, 80, '赤兔马')
    print(lb.name, lb.ride)
