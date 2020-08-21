class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何自定义的变量
        # 绑定在实例身上的属性，在类中任意位置可见可用
        self.name = name
        self.weapon = weapon

    def show_me(self):
        # 绑定在实例身上的属性，在类中任意位置可见可用
        print('我是%s，我擅用%s' % (self.name, self.weapon))

    def speak(self, word):
        # 没有绑定在实例身上的变量，只是局部变量，只能用在函数中
        print(word)

class Weapon:
    def __init__(self, wname, type, strength):
        self.wname = wname
        self.type = type
        self.strength = strength

if __name__ == '__main__':
    ji = Weapon('方天画戟', '物理', 100)
    print(ji.wname, ji.type, ji.strength)
    lb = Role('吕布', ji)
    # print(lb.name, lb.weapon)
    print(lb.weapon.wname, lb.weapon.type, lb.weapon.strength)
    # print(lb.name, lb.weapon)
    # lb.show_me()
    # lb.speak('马中赤兔，人中吕布')



