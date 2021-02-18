stack = []  # 使用列表模拟栈

def push_it():
    "用于压栈"
    data = input("数据: ").strip()
    if data:  # 如果data非空
        stack.append(data)
    else:
        print("未获取到数据。")

def pop_it():
    "用于出栈"
    if stack:  # 如果stack非空
        print("从栈中弹出: \033[31;1m%s\033[0m" % stack.pop())
    else:
        print("\033[31;1m栈已经是空的\033[0m")

def view_it():
    "查询"
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    "用于显示菜单，实现代码逻辑"
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while 1:
        choice = input(prompt).strip()  # 去除用户输入的两端空白字符
        if choice not in ['0', '1', '2', '3']:
            print("无效的输入，请重试。")
            continue

        if choice == '3':
            print('Bye-bye')
            break

        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        else:
            view_it()

if __name__ == '__main__':
    show_menu()
