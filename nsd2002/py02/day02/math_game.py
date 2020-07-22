# 1 + 1 = 2
# Very Good!
# Continue(y/n)? y
# 83 + 65 = 100
# Wrong Answer.
# 83 + 65 = 200
# Wrong Answer.
# 83 + 65 = 150
# Wrong Answer.
# Answer: 83 + 65 = 148
# Continue(y/n)? No
# Bye-bye

def exam():
    "出题，用户作答"
    print('exam')

def main():
    "程序的代码逻辑"
    while 1:
        exam()
        # 获取用户输入，去除两端空格再取出第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'Nn':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()







