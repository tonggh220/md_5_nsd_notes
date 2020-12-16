class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

class Weapon:
    def __init__(self, wname, strength, type):
        self.wname = wname
        self.strength = strength
        self.type = type

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100, '物理')
    print(ji.wname, ji.strength, ji.type)
