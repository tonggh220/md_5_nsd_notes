def isdigit(s):
    "如果字符串s全是数字返回True，否则返回False"
    for ch in s:
        if ch not in '0123456789':
            return False  # 函数遇到return就会结束，将值返回

    return True

if __name__ == '__main__':
    s1 = input('number: ')
    r = isdigit(s1)
    print(r)
