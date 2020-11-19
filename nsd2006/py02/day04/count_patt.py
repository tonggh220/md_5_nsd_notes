import re

def count_patt(fname, patt):
    result = {}
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 如果匹配到了
                key = m.group()
                result[key] = result.get(key, 0) + 1

    return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.567890.10.22 / 202.13.8.56
    br = 'Chrome|MSIE|Firefox'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
