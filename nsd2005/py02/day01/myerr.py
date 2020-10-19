def get_info(name, age):
    if not 0 < age < 120:
        raise ValueError("年龄超过范围(1~119)")
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    try:
        get_info('nb', 200)
    except ValueError as e:  # 将捕获到的异常保存到变量e中
        print(e)
