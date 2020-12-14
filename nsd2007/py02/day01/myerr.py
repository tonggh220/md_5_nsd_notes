def get_info(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超过范围(1~119)')
    print('%s is %s years old' % (name, age))

def get_info2(name, age):
    # 如果0 < age < 120为真，什么也不发生；如果为假，一定会发生AssertionError异常
    assert 0 < age < 120, '年龄超过范围(1~119)'
    print('%s is %s years old' % (name, age))


if __name__ == '__main__':
    # get_info('nb', 200)
    get_info2('plj', 188)
