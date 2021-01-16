import os
import pickle
from time import strftime

def save(fname):
    "用于记录收入"
    # 获取日期、收入、余额和备注这几个字段
    date = strftime('%Y-%m-%d')
    amount = int(input("金额: "))
    comment = input("备注: ")
    # 从文件里取出记账内容
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] + amount
    # 构建收入记录
    record = [date, amount, 0, balance, comment]
    records.append(record)
    # 记录存到文件中
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    "用于记录开销"
    # 获取日期、收入、余额和备注这几个字段
    date = strftime('%Y-%m-%d')
    amount = int(input("金额: "))
    comment = input("备注: ")
    # 从文件里取出记账内容
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] - amount
    # 构建收入记录
    record = [date, 0, amount, balance, comment]
    records.append(record)
    # 记录存到文件中
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    "用于查询收支"
    # 打印表头
    print(
        "%-12s%-8s%-8s%-12s%-20s" %
        ('date', 'save', 'cost', 'balance', 'comment')
    )
    # 取出文件内容，打印
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    for record in records:
        print("%-12s%-8s%-8s%-12s%-20s" % tuple(record))


def show_menu():
    "实现主程序代码逻辑"
    funcs = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 支出
(2) 查账
(3) 退出
请选择(0/1/2/3): """
    fname = 'account.data'
    # 如果用于记账的文件不存在，则初始化它
    if not os.path.exists(fname):
        date = strftime('%Y-%m-%d')
        init_data = [[date, 0, 0, 10000, 'init data']]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'  # 如果用户按下ctrl+c/ctrl+d，则认为用户选择了3

        if choice not in ['0', '1', '2', '3']:
            print("无效的输入，请重试。")
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        funcs[choice](fname)

if __name__ == '__main__':
    show_menu()
