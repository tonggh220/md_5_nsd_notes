# 1 + 1 = 2
# Very Good!
# Continue(Y/n): yes
# 87 - 65 = 10
# Wrong Answer
# 87 - 65 = 20
# Wrong Answer
# 87 - 65 = 1
# Wrong Answer
# The Answer:
# 87 - 65 = 22
# Continue(Y/n): n
# Bye-bye

def exam():
    '用于出题，用户作答'
    print('exam')

def main():
    '主程序代码逻辑'
    while 1:
        exam()
        yn = input('Continue(Y/n)? ').strip()[0]  # 取出用户输入的第一个非空字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
