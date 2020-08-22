import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        '用于在fname中统计patt出现的次数'
        cpatt = re.compile(patt)  # 编译，以便有更好的匹配效率
        patt_dict = {}  # 定义保存模式出现次数的字典
        # 遍历文件，在文件中匹配模式，记录到字典中
        with open(self.fname) as fobj:
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
    cp = CountPatt(fname)
    result1 = cp.count_patt(ip)
    result2 = cp.count_patt(br)
    print(result1)
    print(result2)
