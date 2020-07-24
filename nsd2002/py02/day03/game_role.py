class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何自定义的变量
        self.name = name
        self.weapon = weapon

if __name__ == '__main__':
    # 实例本身将会自动作为第一个参数传递，本例中是lb
    lb = Role('吕布', '方天画戟')  # 实例化，创建具体的对象
    print(lb.name, lb.weapon)
