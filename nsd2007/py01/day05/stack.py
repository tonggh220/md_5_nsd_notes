def push_it():
    "用于压栈"
    print('push')

def pop_it():
    "用于出栈"
    print('pop')

def view_it():
    "查询"
    print('view')

def show_menu():
    "用于显示菜单，实现代码逻辑"
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while 1:
        choice = input(prompt).strip()  # 去除用户输入的两端的空格
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('Bye-bye')
            break

        # 根据用户的选择，调用相关函数
        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        else:
            view_it()

if __name__ == '__main__':
    show_menu()
