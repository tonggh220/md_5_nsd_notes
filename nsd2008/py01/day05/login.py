userdb = {}

def register():
    '用于新用户注册'
    user = input("username: ").strip()
    if user == "":
        print("用户名不能为空")
    elif user in userdb:
        print("用户已存在")
    else:
        password = input("password: ")
        userdb[user] = password
        print("注册成功")

def login():
    '用于登陆'

def show_menu():
    '程序主体，实现代码逻辑'
    funcs = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print("无效的输入，请重试。")
            continue

        if choice == '2':
            print('Bye-bye')
            break

        funcs[choice]()

if __name__ == '__main__':
    show_menu()
