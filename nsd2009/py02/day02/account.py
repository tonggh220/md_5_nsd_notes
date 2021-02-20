import os
import pickle
from time import strftime

def save(fname):
    "用于记录收入"
    date = strftime('%Y-%m-%d')
    try:
        amount = int(input("金额: "))
        comment = input("备注: ")
    except (KeyboardInterrupt, EOFError):
        print("\nBye-bye")
        exit(1)
    except ValueError:
        print("无效的金额")
        return  # return类似于循环的break，它结束函数，默认返回None

    # 在文件中取出所有收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] + amount
    # 将最新一笔收入追加到大列表中，并保存至文件
    records.append([date, amount, 0, balance, comment])
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    "用于记录支出"
    date = strftime('%Y-%m-%d')
    try:
        amount = int(input("金额: "))
        comment = input("备注: ")
    except (KeyboardInterrupt, EOFError):
        print("\nBye-bye")
        exit(1)
    except ValueError:
        print("无效的金额")
        return

    # 在文件中取出所有收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] - amount
    # 将最新一笔支出追加到大列表中，并保存至文件
    records.append([date, 0, amount, balance, comment])
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    "用于查询收支"
    # 在文件中取出所有收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 打印表头
    print('%-15s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # 打印收支记录
    for record in records:
        print('%-15s%-8s%-8s%-12s%-20s' % tuple(record))

def show_menu():
    "程序主体代码逻辑"
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
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'  # 如果用户按下ctrl+c/ctrl+d则认为他选了3

        if choice not in ['0', '1', '2', '3']:
            print("无效的输入，请重试。")
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        funcs[choice](fname)

if __name__ == '__main__':
    show_menu()
