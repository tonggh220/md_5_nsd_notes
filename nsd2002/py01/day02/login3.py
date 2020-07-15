# 不要右击运行，要在真正的终端中运行
import getpass

username = input('username: ')
password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('login successful')
else:
    print('login failed')
