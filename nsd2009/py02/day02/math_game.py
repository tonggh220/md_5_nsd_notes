def exam():
    "用于出题，让用户作答"
    print('exam')

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        # 去除字符串两端空格后，取第一个字符
        choice = input("Continue(y/n)? ").strip()[0]
        if choice in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
