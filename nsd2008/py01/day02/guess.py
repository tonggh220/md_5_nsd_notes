import random
# 随机生成1~100以内的整数，可以包含1和100
n = random.randint(1, 100)
i = 0  # 定义计数器
# 猜答案, 给用户最多7次机会，提示用户猜大了还是猜小了
while i < 7:
    i += 1
    answer = int(input("guess the number: "))
    if answer > n:
        print("猜大了")
    elif answer < n:
        print("猜小了")
    else:
        print("猜对了")
        break
print("The Answer:", n)
