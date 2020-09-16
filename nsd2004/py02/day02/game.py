# 1 + 1 = 2
# Very Good!!!
# Continue(y/n)? y
# 97+ 65 = 100
# Wrong Answer.
# 97+ 65 = 200
# Wrong Answer.
# 97+ 65 = 300
# Wrong Answer.
# The Answer:
# 97+ 65 = 162
# Continue(y/n)? n
# Bye-bye

def exam():
    "用于出题，让用户作答"
    print('exam')

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        # 去除得到的字符串两端的空格后，取第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
