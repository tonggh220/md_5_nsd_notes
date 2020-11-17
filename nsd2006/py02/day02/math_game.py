def exam():
    "出题，用户作答"
    print('exam')

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        yn = input("Continue(y/n)? ").strip()[0]  # 去除两端空格后，取第一个字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
