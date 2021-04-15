import getpass  # 导入getpass模块

username = input('username: ')
password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('Login Successful')
else:
    print('Login Failed')
