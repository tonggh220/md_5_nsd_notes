import re

def count_patt(fname, patt):
    "在给定的文件fname中，统计各种模式出现的次数"


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1.234.5678.9091  202.13.5.129
    br = 'Chrome|Firefox|MSIE'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)


