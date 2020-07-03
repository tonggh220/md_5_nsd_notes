userdb = {}

def register():
    "用于注册用户"
    username = input('username: ').strip()
    if not username:  # 如果用户名为空
        print('用户名不能为空')
    elif username in userdb:
        print('用户已存在')
    else:
        password = input('password: ')
        userdb[username] = password

def login():
    "用于登陆"
    username = input('username: ').strip()
    password = input('password: ')
    # if username in userdb and userdb[username] == password:
    if userdb.get(username) == password:
        print('登陆成功')
    else:
        print('登陆失败')


def show_menu():
    "用于显示菜单"
    funcs = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """

    while 1:
        xz = input(prompt).strip()
        if xz not in ['0', '1', '2']:
            print('无效的选择，请重试。')
            continue

        if xz == '2':
            print('Bye-bye')
            break

        funcs[xz]()


if __name__ == '__main__':
    show_menu()
