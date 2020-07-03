class Role:
    def __init__(self, name, weapon, clothes, shoes, hair):
        "构造器方法，用于绑定数据到实例身上"
        self.name = name
        self.weapon = weapon
        self.clothes = clothes
        self.shoes = shoes
        self.hair = hair

class Warrior(Role):
    def __init__(self, name, weapon, clothes, shoes, hair, ride):
        # Role.__init__(self, name, weapon, clothes, shoes, hair)  # 也可写作下面方式
        super(Warrior, self).__init__(name, weapon, clothes, shoes, hair)
        self.ride = ride

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟', '亮银甲', '运动鞋', '黑发', '赤兔马')
    print(lb.name, lb.ride)
