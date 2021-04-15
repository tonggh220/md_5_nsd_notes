import random

# 随机生成100以内的整数
num = random.randint(1, 100)

i = 0
# 给用户最多7次机会
while i < 7:
    i += 1
    answer = int(input("猜数(1~100): "))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
else:  # 循环被break则不执行else语句。循环由于条件不满足结束时才执行else语句
    print(f'正确答案是: {num}')
