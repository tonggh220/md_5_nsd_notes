def push_it():
    "用于压栈"
    print('push push')

def pop_it():
    "用于出栈"
    print('pop pop')

def view_it():
    "查询"
    print('view view')

def show_menu():
    "用于显示菜单，实现代码逻辑"
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

        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        elif choice == '2':
            view_it()
        else:
            print('Bye-bye')
            break

if __name__ == '__main__':
    show_menu()
