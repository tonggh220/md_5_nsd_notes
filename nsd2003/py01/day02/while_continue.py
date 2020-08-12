# 计算100以内偶数之和
# 定义一个保存最终结果的变量
result = 0
# 定义一个计数器
i = 0

while i < 100:
    i += 1       # i的值自增1
    if i % 2 == 1:
        continue
    else:
        result += i  # 不断的把i的值累加到result中

print(result)
