stack = []

def push_it():
    "用于将数据压入栈"
    data = input('数据: ').strip()  # 去除字符串两端空格
    if data:  # 如果字符串非空
        stack.append(data)
    else:
        print('\033[31;1m请输入非空白字符串\033[0m')

def pop_it():
    "用于将数据从栈弹出"
    if stack:  # 如果列表非空
        print('\033[34;1m从列表中，弹出了: %s\033[0m' % stack.pop())
    else:
        print('\033[31;1m栈是空的\033[0m')

def view_it():
    "用于查询"
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    "用于显示菜单，根据用户的选择，不断调用其他函数"
    # 将函数存入到字典，函数后面不要加()，如果加()是把函数的返回值存入字典
    funcs = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while 1:
        xz = input(prompt).strip()
        if xz not in ['0', '1', '2', '3']:
            print('\033[31;1m无效的选择，请重试。\033[0m')
            continue

        if xz == '3':
            print('Bye-bye')
            break

        funcs[xz]()  # 在字典中取出函数并调用

if __name__ == '__main__':
    show_menu()
