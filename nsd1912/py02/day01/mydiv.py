# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
#     print('Done')
# except ValueError:
#     print('请输入非0数字')
# except ZeroDivisionError:
#     print('请输入非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
###############################

# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e中
#     print('请输入非0数字:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

###############################

# try:
#     n = int(input('number: '))
#     result = 100 / n
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e中
#     print('请输入非0数字:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
# else:
#     print(result)
#
# print('Done')

###############################

# try:
#     n = int(input('number: '))
#     result = 100 / n
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e中
#     print('请输入非0数字:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
#     exit(1)  # 程序遇到exit将会彻底结束
# else:
#     print(result)
#
# print('Done')

###############################

try:
    n = int(input('number: '))
    result = 100 / n
except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e中
    print('请输入非0数字:', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(1)  # 程序遇到exit将会彻底结束
else:
    print(result)
finally:
    print('异常处理语句结束')

print('Done')
