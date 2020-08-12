import getpass

username = input('username: ')
password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('\033[32;1m登陆成功\033[0m')
else:
    print('\033[31;1m登陆失败\033[0m')
