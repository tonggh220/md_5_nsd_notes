import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        # 定义用于保存结果的变量
        patt_dict = {}
        # 为了有更好的匹配效率，可以将模式字符串先编译
        cpatt = re.compile(patt)

        # 遍历文件，在每一行匹配模式字符串
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到返回匹配对象，为真
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    weblog = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.6789.543.10 100.201.54.3
    br = 'Chrome|Firefox|MSIE'
    cp1 = CountPatt(weblog)
    result1 = cp1.count_patt(ip)
    result2 = cp1.count_patt(br)
    print(result1)
    print(result2)
