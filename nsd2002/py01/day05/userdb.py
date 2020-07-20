userdb = {}

def register():
    "注册"
    username = input("username: ").strip()
    if username == '':
        print('用户名必须非空')
    elif username in userdb:
        print('用户已存在')
    else:
        password = input("password: ")
        userdb[username] = password

def login():
    "登陆"

def show_menu():
    "显示菜单"
    funcs = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """

    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效的输入，请重试。')
            continue

        if choice == '2':
            print('Bye-bye')
            break

        funcs[choice]()

if __name__ == '__main__':
    show_menu()
