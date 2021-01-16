# 1 + 1 = 2
# Very Good!!!
# Continue(y/n)? y
# 28 + 36 = 40
# Wrong Answer!!!
# 28 + 36 = 100
# Wrong Answer!!!
# 28 + 36 = 50
# Wrong Answer!!!
# The Answer: 28 + 36 = 64
# Continue(y/n)? n
# Bye-bye

def exam():
    "用于出题，用户作答"
    print('exam')

def main():
    "用于主程序代码逻辑"
    while 1:
        exam()
        # 去除字符串两端空格后，取出第一个字符
        yn = input("Continue(y/n)? ").strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()






