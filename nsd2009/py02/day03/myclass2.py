class Weapon:
    def __init__(self, wname, strength, type):
        self.wname = wname
        self.strength = strength
        self.type = type

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100, '物理')
    print(ji.wname, ji.strength, type)
