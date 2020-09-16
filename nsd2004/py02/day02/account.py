import pickle
import os
from time import strftime

def save(fname):
    "用于记录收入"
    date = strftime('%Y-%m-%d')
    amount = int(input('金额: '))
    comment = input('备注: ')
    # 在文件中取出全部的收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount  # 计算最新余额
    record = [date, amount, 0, balance, comment]  # 构建最新一笔记录
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    "用于记录开销"

def query(fname):
    "用于显示收支记录"

def show_menu():
    "程序主体，实现代码逻辑"
    funcs = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    fname = 'account.data'
    if not os.path.exists(fname):
        init_data = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']]
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

        funcs[choice](fname)

if __name__ == '__main__':
    show_menu()
