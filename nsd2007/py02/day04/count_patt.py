import re

def count_patt(fname, patt):
    "在给定的文件fname中，统计各种模式出现的次数"
    result = {}
    cpatt = re.compile(patt)  # 为了更好的执行效率，把模式编译
    # 在文件中的每一行匹配模式，匹配到就存入字典
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m != None:  # 如果匹配结果不是None
                key = m.group()
                result[key] = result.get(key, 0) + 1

    return result


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1.234.5678.9091  202.13.5.129
    br = 'Chrome|Firefox|MSIE'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)


