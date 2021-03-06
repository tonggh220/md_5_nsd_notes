import os
import pickle
from time import strftime


def save(fname):
    "用于记录收入"
    try:
        amount = int(input("金额: "))
        comment = input("备注: ")
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit(1)  # 如果用户按下ctrl+c/ctrl+d，彻底结束程序
    except ValueError:
        print("无效的金额")
        return  # 函数的return类似于循环的break，一旦遇到return函数就会结束，返回到调用者，默认返回None

    date = strftime('%Y-%m-%d')
    # 在文件中取出全部的收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 计算最新余额
    balance = records[-1][-2] + amount
    # 构建最新一笔收入记录，并追加到记录列表中
    record = [date, amount, 0, balance, comment]
    records.append(record)
    # 因为records列表拥有所有的收支记录，所以可以将它直接写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)


def cost(fname):
    "用于记录开销"
    try:
        amount = int(input("金额: "))
        comment = input("备注: ")
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit(1)  # 如果用户按下ctrl+c/ctrl+d，彻底结束程序
    except ValueError:
        print("无效的金额")
        return

    date = strftime('%Y-%m-%d')
    # 在文件中取出全部的收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 计算最新余额
    balance = records[-1][-2] - amount
    # 构建最新一笔收入记录，并追加到记录列表中
    record = [date, 0, amount, balance, comment]
    records.append(record)
    # 因为records列表拥有所有的收支记录，所以可以将它直接写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)


def query(fname):
    "用于查询收支记录"
    # 取出文件中的收支记录，再把每行记录打印出来
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印表头
    print('%-15s%-8s%-8s%-12s%-20s' %
          ('date', 'save', 'cost', 'balance', 'comment'))

    # 在大列表records中取出每一个小列表，也就是每行记录，打印
    for record in records:
        print('%-15s%-8s%-8s%-12s%-20s' % tuple(record))

def show_menu():
    "主程序逻辑代码"
    funcs = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    fname = 'account.data'  # 用于保存记录的文件名
    # 如果文件不存在，则初始化它
    if not os.path.exists(fname):
        init_data = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'   # 如果用户按下ctrl+c/ctrl+d，认为它选择了3

        if choice not in ['0', '1', '2', '3']:
            print("无效的选择，请重试。")
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        funcs[choice](fname)


if __name__ == '__main__':
    show_menu()
