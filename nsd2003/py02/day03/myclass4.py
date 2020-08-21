class Role:
    def __init__(self, name, weapon, gender, menpai):
        self.name = name
        self.weapon = weapon
        self.gender = gender
        self.menpai = menpai

class Warrior(Role):
    def __init__(self, name, weapon, gender, menpai, qq):
        # Role.__init__(self, name, weapon, gender, menpai)
        super(Warrior, self).__init__(name, weapon, gender, menpai)
        self.qq = qq

if __name__ == '__main__':
    lb = Warrior('lvbu', 'ji', 'male', 'ziji', '23423554')
