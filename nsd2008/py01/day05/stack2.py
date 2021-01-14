stack = []  # 全局变量从定义开始到结束部分，总是可见可用

def push_it():
    "用于压栈"
    data = input("数据: ").strip()
    if data:  # 如果data非空
        stack.append(data)
    else:
        print("没有获取到数据")

def pop_it():
    "用于出栈"
    if stack:  # 如果列表非空
        data = stack.pop()
        print("从栈中弹出了: %s" % data)
    else:
        print("栈已经为空")

def view_it():
    "查询"
    print('%s' % stack)

def show_menu():
    "用于显示菜单，实现代码逻辑"
    # 将函数存入字典
    funcs = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while 1:
        choice = input(prompt).strip()  # 去除两端用户输入的空白字符
        if choice not in ['0', '1', '2', '3']:
            print("无效的输入，请重试。")
            continue

        if choice == '3':
            print('Bye-bye')
            break
        # 根据choice的值取出字典中的函数，并调用
        funcs[choice]()

if __name__ == '__main__':
    show_menu()
