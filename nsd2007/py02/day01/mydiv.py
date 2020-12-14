try:
    num = int(input("number: "))
    result = 100 / num
    print(result)
    print('Done')
except ValueError:
    print("必须输入非0数字")
