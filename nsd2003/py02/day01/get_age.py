def get_age(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超过范围(1~119)')
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    try:
        get_age('nb', 200)
    except ValueError as e:
        print('Error:', e)


