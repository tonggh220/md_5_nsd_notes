result = 0
i = 0

while i < 100:
    i += 1
    if i % 2:  # i%2的结果只有1和0两种情况，0为假，非0为真
        continue
    result += i

print(result)
