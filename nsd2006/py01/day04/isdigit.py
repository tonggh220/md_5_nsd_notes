num = input("number: ")   # 12345678  123a456

for ch in num:
    if ch not in '0123456789':
        print('不全是数字')
        break
else:
    print('是数字')
