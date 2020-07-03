def isdigit(s):
    "如果字符串中所有的字符都是数字返回True，否则返回False"
    for ch in s:
        if ch not in '0123456789':
            return False

    return True

if __name__ == '__main__':
    s1 = input("输入数字: ")
    print(isdigit(s1))
