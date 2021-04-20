stack = []  # 使用列表模拟栈

def push_it():
    "用于压栈"
    data = input('数据: ').strip()
    if data:  # 如果data非空
        stack.append(data)
    else:
        print('\033[31;1m没有获取到数据\033[0m')

def pop_it():
    "用于出栈"
    if stack:  # 如果stack非空
        # data = stack.pop()
        print(f'从栈中弹出了: \033[31;1m{stack.pop()}\033[0m')
    else:
        print('\033[31;1m栈已经为空\033[0m')

def view_it():
    "查询"
    print(f'\033[32;1m{stack}\033[0m')

def show_menu():
    "用于显示菜单，实现代码逻辑"
    # 将函数存入字典
    funcs = {'0': push_it, '1': pop_it, '2': view_it}
    # 定义菜单
    prompt = '''(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): '''

    while 1:
        choice = input(prompt).strip()  # 去除字符串两端空格
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('Bye-bye')
            break

        funcs[choice]()

if __name__ == '__main__':
    show_menu()
