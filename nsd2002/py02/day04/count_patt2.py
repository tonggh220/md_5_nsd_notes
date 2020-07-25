import re

class CountPatt:
    def count_patt(self, fname, patt):
        # 为了有更好的匹配效率，先将模式编译
        cpatt = re.compile(patt)
        # 创建用于保存结果的变量
        patt_dict = {}

        # 遍历文件，在每一行找到模式，并统计出现的次数
        with open(fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到了，返回匹配对象，非空对象为真
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.56789.1.10  123.12.18.3
    br = 'Chrome|Firefox|MSIE'
    cp = CountPatt()
    result1 = cp.count_patt(fname, ip)
    result2 = cp.count_patt(fname, br)
    print(result1)
    print(result2)
