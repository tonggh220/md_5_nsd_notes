import re

def count_patt(fname, patt):
    '用于在fname中统计patt出现的次数'
    cpatt = re.compile(patt)  # 编译，以便有更好的匹配效率
    patt_dict = {}  # 定义保存模式出现次数的字典
    # 遍历文件，在文件中匹配模式，记录到字典中
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 如果得到了匹配对象
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1

    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.678.90.2
    br = 'Chrome|MSIE|Firefox'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
