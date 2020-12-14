# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except ValueError:
#     print("必须输入非0数字")
# except ZeroDivisionError:
#     print("必须输入非0数字")
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')

# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError):
#     print("必须输入非0数字")
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError) as e:  # 把异常保存到变量e
#     print("必须输入非0数字:", e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')


try:
    num = int(input("number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:  # 把异常保存到变量e
    print("必须输入非0数字:", e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
else:   # 只有不发生异常时，才会执行else语句
    print(result)

print('Done')
