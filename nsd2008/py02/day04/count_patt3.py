import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        "在给定的文件fname中，统计模式字符串patt出现的次数"
        patt_dict = {}
        cpatt = re.compile(patt)
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果可以匹配到，是非空对象，为真；没有匹配到返回None，为假
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.5678.1.23 192.168.1.23
    br = 'Chrome|Firefox|MSIE'
    cp1 = CountPatt(fname)
    result1 = cp1.count_patt(ip)
    result2 = cp1.count_patt(br)
    print(result1)
    print(result2)
