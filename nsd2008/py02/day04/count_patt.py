import re

def count_patt(fname, patt):
    "在给定的文件fname中，统计模式字符串patt出现的次数"
    # 定义用于保存结果的变量
    patt_dict = {}
    # 为了更好的效率，可以把模式进行编译
    cpatt = re.compile(patt)
    # 在文件的每一行中匹配模式，如果匹配到，则更新字典
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 如果可以匹配到，是非空对象，为真；没有匹配到返回None，为假
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1

    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d'  # 1234.5678.1.23 192.168.1.23
    br = 'Chrome|Firefox|MSIE'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
