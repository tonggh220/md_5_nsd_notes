try:
    num = int(input("number: "))
    result = 100 / num
    print(result)
    print('Done')
except ValueError:
    print('请输入非0数字')
