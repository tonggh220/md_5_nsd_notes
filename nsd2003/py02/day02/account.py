import os
import pickle
from time import strftime

def save(fname):
    '记录收入'
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 从文件中取出所有记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount  # 计算最新余额
    # 构建最新一笔记录
    record = [date, amount, 0, balance, comment]
    records.append(record)
    # 将更新后的记录写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    '记录开销'
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 从文件中取出所有记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] - amount  # 计算最新余额
    # 构建最新一笔记录
    record = [date, 0, amount, balance, comment]
    records.append(record)
    # 将更新后的记录写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    '查询收支情况'
    # 从文件中取出所有记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 打印表头
    print('%-14s%-8s%-8s%-10s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # 打印每行记录
    for record in records:
        print('%-14s%-8s%-8s%-10s%-20s' % tuple(record))

def show_menu():
    '程序主体代码逻辑'
    funcs = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    fname = 'account.data'  # 如果记账文件不存在，则初始化它
    if not os.path.exists(fname):
        init_data = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        funcs[choice](fname)

if __name__ == '__main__':
    show_menu()
