# 10 + 8 = 18
# Very Good!
# Continue(y/n)? y
# 23 + 12 = 30
# Wrong Answer!
# 23 + 12 = 40
# Wrong Answer!
# 23 + 12 = 50
# Wrong Answer!
# The Answer:
# 23 + 12 = 35
# Continue(y/n)? n
# Bye-bye

def exam():
    "出题，用户作答"
    print('exam')

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        yn = input("Continue(y/n)? ").strip()[0]  # 去除字符串两端空白字符后，取第一个字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()






