# 100以内偶数之和
# 定义用于保存结果的变量
result = 0
# 定义累加计数器
i = 0

while i < 100:
    i += 1
    if i % 2:  # i%2的结果只有0和1两种情况，0为假，1为真
        continue
    result += i

print(result)
