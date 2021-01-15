# try:
#     n = int(input("number: "))
#     result = 100 / n
#     print(result)
#     print('Done')
# except ValueError:
#     print("请输入非0数字")
# except ZeroDivisionError:
#     print("请输入非0数字")
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')

try:
    n = int(input("number: "))
    result = 100 / n
    print(result)
    print('Done')
except (ValueError, ZeroDivisionError):
    print("请输入非0数字")
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')












