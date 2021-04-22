'''
1 + 1 = 2
Very Good!!!
Continue(Y/n)? y
34 + 52 = 100
Wrong Answer!!!
34 + 52 = 10
Wrong Answer!!!
34 + 52 = 200
Wrong Answer!!!
The Answer:
34 + 52 = 86
Continue(Y/n)? no
Bye-bye
'''

def exam():
    '用于出题，用户作答'
    print('exam')

def main():
    '主程序代码逻辑'
    while 1:
        exam()
        yn = input('Continue(Y/n)? ').strip()[0]  # 取出第一个字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
