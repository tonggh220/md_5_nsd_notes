import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        # 为了有更好的执行效率，先把模式编译
        cpatt = re.compile(patt)
        result = {}  # 定义用于保存结果的字典

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    result[key] = result.get(key, 0) + 1

        return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.567789.12.1  192.168.10.8
    br = 'Firefox|MSIE|Chrome'
    cp1 = CountPatt(fname)
    result1 = cp1.count_patt(ip)
    result2 = cp1.count_patt(br)
    print(result1)
    print(result2)
