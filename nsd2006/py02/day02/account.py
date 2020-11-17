import os
import pickle
from time import strftime

def save():
    "用于记录收入"
    print('save')

def cost():
    "用于记录开销"
    print('cost')

def query():
    "用于查询收支情况"
    print('query')

def show_menu():
    "主程序代码逻辑"
    funcs = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    fname = "account.data"
    # 如果记账文件不存在，需要初始化它
    if not os.path.exists(fname):
        init_data = [[strftime("%Y-%m-%d"), 0, 0, 10000, "init data"]]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)
            
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print("无效的输入，请重试。")
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        funcs[choice]()

if __name__ == '__main__':
    show_menu()

