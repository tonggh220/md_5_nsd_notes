def set_info(name, age):
    if not 1 <= age <= 120:
        raise ValueError('年龄超过范围(1~120)')
    print('%s is %s years old.' % (name, age))

def set_info2(name, age):
    assert 1 <= age <= 120, '年龄超过范围(1~120)'
    print('%s is %s years old.' % (name, age))

if __name__ == '__main__':
    try:
        set_info('牛老师', 200)
    except ValueError as e:
        print('Error:', e)

    set_info2('庞老师', 188)
