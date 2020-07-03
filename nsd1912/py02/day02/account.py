from time import strftime
import os
import pickle

def save(fname):
    "用于记录收入"
    try:
        jin_e = int(input('金额: '))
        beizhu = input('备注: ')
    except ValueError:
        print('请输入金额。')
        return
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit(1)

    date = strftime('%Y-%m-%d')
    # 从文件中取出全部记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    yu_e = records[-1][-2] + jin_e

    # 将最新一笔收入追加到列表中
    record = [date, jin_e, 0, yu_e, beizhu]
    records.append(record)

    # 将收支情况列表写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    "用于记录支出"
    try:
        jin_e = int(input('金额: '))
        beizhu = input('备注: ')
    except ValueError:
        print('请输入金额。')
        return
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit(1)

    date = strftime('%Y-%m-%d')
    # 从文件中取出全部记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    yu_e = records[-1][-2] - jin_e

    # 将最新一笔开销追加到列表中
    record = [date, 0, jin_e, yu_e, beizhu]
    records.append(record)

    # 将收支情况列表写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    "用于查看收支情况"
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印表头
    print('%-12s%-8s%-8s%-10s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # 从大列表中取出小列表，再将小列表转成元组进行打印
    for record in records:
        print('%-12s%-8s%-8s%-10s%-20s' % tuple(record))

def show_menu():
    "用于显示菜单"
    funcs = {'0': save, '1': cost, '2': query}
    prompt = """(0) 记录收入
(1) 记录支出
(2) 查询收支
(3) 退出
请选择(0/1/2/3): """
    fname = 'account.data'
    if not os.path.exists(fname):  # 如果记账文件不存在，则初始化它
        init_data = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        try:
            xz = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            xz = '3'

        if xz not in ['0', '1', '2', '3']:
            print('无效的选择，请重试。')
            continue

        if xz == '3':
            print('\nBye-bye')
            break

        funcs[xz](fname)


if __name__ == '__main__':
    show_menu()
