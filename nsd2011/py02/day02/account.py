import pickle
import os
from time import strftime

def save(fname):
    '用于记录收入'
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit()
    except ValueError:
        print('请输入正确的金额')
        return  # 函数的return像循环的break，将会提前结束函数，默认返回None

    date = strftime('%Y-%m-%d')
    # 取出收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] + amount
    # 构建最新一笔收入
    record = [date, amount, 0, balance, comment]
    # 追加最新的记录到records
    records.append(record)
    # 回写文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    '用于记录开销'
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit()
    except ValueError:
        print('请输入正确的金额')
        return  # 函数的return像循环的break，将会提前结束函数，默认返回None

    date = strftime('%Y-%m-%d')
    # 取出收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] - amount
    # 构建最新一笔支出
    record = [date, 0, amount, balance, comment]
    # 追加最新的记录到records
    records.append(record)
    # 回写文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    '用于查询收支记录'
    # 取出收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印表头
    print(f'{"date":<15}{"save":<8}{"cost":<8}{"balance":<12}{"comment":<20}')
    # 在records中取出每一行记录并打印
    for record in records:
        print(f'{record[0]:<15}{record[1]:<8}{record[2]:<8}{record[3]:<12}{record[4]:<20}')

def show_menu():
    '主程序代码逻辑'
    funcs = {'0': save, '1': cost, '2': query}
    prompt = '''(0) 收入
(1) 支出
(2) 查账
(3) 退出
请选择(0/1/2/3/): '''
    fname = 'account.data'
    # 记账文件如果不存在，则初始化它
    if not os.path.exists(fname):
        init_data = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'  # 用户按了ctrl+c或ctrl+d，算他选了3

        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        funcs[choice](fname)

if __name__ == '__main__':
    show_menu()
