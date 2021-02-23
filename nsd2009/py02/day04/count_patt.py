import re

def count_patt(fname, patt):
    # 为了更好的执行效率，编译正则模式字符串
    cpatt = re.compile(patt)
    # 定义保存结果的变量
    result = {}
    # 从文件中找到匹配项，并保存
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 没有匹配到返回None，为假；匹配到返回匹配对象，为真
                k = m.group()
                result[k] = result.get(k, 0) + 1
    return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.0.2345.29  192.168.1.25
    br = 'Chrome|Firefox|MSIE'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
