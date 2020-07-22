import os
import pickle
from time import strftime

def save(fname):
    "存钱"
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 在文件中取出所有的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] + amount
    # 将收入情况存入列表
    record = [date, amount, 0, balance, comment]
    records.append(record)
    # 将更新后的列表再存入文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    "开销"
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 在文件中取出所有的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] - amount
    # 将收入情况存入列表
    record = [date, 0, amount, balance, comment]
    records.append(record)
    # 将更新后的列表再存入文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    "查询"
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balanace', 'comment'))
    for record in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(record))

def show_menu():
    "程序执行逻辑"
    funcs = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 支出
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
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        funcs[choice](fname)

if __name__ == '__main__':
    show_menu()
