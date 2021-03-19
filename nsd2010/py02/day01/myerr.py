def get_info(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超出范围(1~119)')
    print(f'{name} is {age} years old.')

def get_info2(name, age):
    assert 0 < age < 120, '年龄超出范围(1~119)'
    print(f'{name} is {age} years old.')

if __name__ == '__main__':
    get_info('nb', 20)
    get_info2('plj', 188)
