# 定义保存结果的变量
result = 0
# 定义计数器
i = 1

while i < 101:
    result += i   # 计数器累加到结果变量
    i += 1        # i -> 2 -> 3 -> 4 -> 5 -> ... -> 101

print(result)
