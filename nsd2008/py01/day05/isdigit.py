def isdigit(s):
    "如果字符串s中的所有字符都是数字返回True，否则返回False"
    for ch in s:
        if ch not in '0123456789':
            # 函数的return类似于循环的break，函数遇到return就会结束
            return False

    return True  # 函数可以有多个return，但是只有一个可以执行

if __name__ == '__main__':
    s1 = input("number: ")
    result = isdigit(s1)
    print(result)
