class Weapon:
    def __init__(self, wname, type, strength):
        self.wname = wname
        self.type = type
        self.strength = strength

class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何自定义的变量
        # 绑定在实例身上的属性，在类中任意位置可见可用
        self.name = name
        self.weapon = weapon

    def show_me(self):
        # 绑定在实例身上的属性，在类中任意位置可见可用
        print('我是%s，擅用%s' % (self.name, self.weapon))

    def speak(self, words):
        # 没有绑定在实例身上的变量，只是局部变量，只能用在函数中
        hh = 'HeHe'
        print(hh)
        print(words)

if __name__ == '__main__':
    ji = Weapon('方天画戟', type='物理', strength=100)
    print(ji.wname, ji.type, ji.strength)
    # 实例本身将会自动作为第一个参数传递，本例中是lb
    lb = Role('吕布', ji)  # 实例化，创建具体的对象
    print(lb.name, lb.weapon.wname, lb.weapon.type, lb.weapon.strength)
    # lb.show_me()
    # lb.speak('马中赤兔，人中吕布')
