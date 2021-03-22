
def save():
    '用于记录收入'
    print('save')

def cost():
    '用于记录开销'
    print('cost')

def query():
    '用于查账'
    print('query')

def show_menu():
    '显示主菜单'
    funcs = {'0': save, '1': cost, '2': query}
    prompt = '''(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): '''

    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        funcs[choice]()

if __name__ == '__main__':
    show_menu()



