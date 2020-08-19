def exam():
    '用于出题，让用户作答'
    print('exam')

def main():
    while 1:
        exam()
        # 去除用户输入的额外空格，并取第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
