# 1 + 1 = 2
# Very Good!
# Continue(y/n)? yes
# 18 + 25 = 30
# Wrong Answer
# 18 + 25 = 40
# Wrong Answer
# 18 + 25 = 50
# Wrong Answer
# The Answer:
# 18 + 25 = 43
# Continue(y/n)? n
# Bye-bye

def exam():
    "出题，用户作答"
    print('exam')

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        yn = input("Continue(y/n)? ").strip()[0]  # 取用户输入的第一个非空格字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
