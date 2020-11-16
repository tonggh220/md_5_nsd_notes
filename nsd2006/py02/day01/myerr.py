def get_info(name, age):
    if not 0 < age < 120:
        raise ValueError("年龄超出范围(1~119)")
    print('%s is %s years old' % (name, age))

def get_info2(name, age):
    assert 0 < age < 120, "年龄超出范围(1~119)"
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    try:
        name = input("name: ")
        age = int(input("age: "))
        get_info(name, age)
        get_info2('plj', 188)
    except (ValueError, AssertionError) as e:
        print('Error:', e)
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit(1)
