import re

class CountPatt:
    def count_patt(self, fname, patt):
        '在一个文件中，统计某个模式字符串出现的次数'
        cpatt = re.compile(patt)  # 编译模式字符串，以便有更好的匹配效率
        patt_dict = {}

        with open(fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到了，返回匹配对象，否则返回None
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 60.0.3112.113  100.1.234.80
    br = ' Chrome|Firefox|MSIE'
    cp = CountPatt()
    result1 = cp.count_patt(fname, ip)
    result2 = cp.count_patt(fname, br)
    print(result1)
    print(result2)
