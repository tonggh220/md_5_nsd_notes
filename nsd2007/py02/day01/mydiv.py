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

try:
    num = int(input("number: "))
    result = 100 / num
    print(result)
    print('Done')
except (ValueError, ZeroDivisionError):
    print("必须输入非0数字")
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')



