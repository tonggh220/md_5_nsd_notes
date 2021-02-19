# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except ValueError:
#     print('请输入非0数字')
# except ZeroDivisionError:
#     print('请输入非0数字')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')
#################################
# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError):
#     print('请输入非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
#################################
# try:
#     num = int(input("number: "))
#     result = 100 / num
# except (ValueError, ZeroDivisionError):
#     print('请输入非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
# else:
#     print(result)
#
# print('Done')
#################################
# try:
#     num = int(input("number: "))
#     result = 100 / num
# except (ValueError, ZeroDivisionError):
#     print('请输入非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
#     exit(1)  # 程序遇到exit，将会结束，退出码$?指定为1
# else:
#     print(result)
#
# print('Done')
#################################
try:
    num = int(input("number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('请输入非0数字')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(1)  # 程序遇到exit，将会结束，退出码$?指定为1
else:
    print(result)
finally:  # 不管异常是否发生，都要执行的语句
    print('Done')
