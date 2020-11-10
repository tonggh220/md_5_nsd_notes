result = 0
i = 0

while i < 100:
    i += 1
    if i % 2:  # 整数除以2余数只有0和1两种情况，1为真，0为假
        continue
    result += i

print(result)
