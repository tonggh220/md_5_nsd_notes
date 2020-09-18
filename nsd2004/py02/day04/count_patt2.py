import re

class CountPatt:
    def count_patt(self, fname, patt):
        result = {}  # 定义用于保存结果的字典
        cpatt = re.compile(patt)  # 将模式字符串先编译将会有更好的匹配效率
        # 在文件的每一行中匹配模式，匹配到就更新到字典中
        with open(fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 非空对象为真
                    key = m.group()
                    result[key] = result.get(key, 0) + 1

        return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.6789.10.8  192.168.10.3
    br = 'Firefox|Chrome|MSIE'
    cp = CountPatt()
    result1 = cp.count_patt(fname, ip)
    result2 = cp.count_patt(fname, br)
    print(result1)
    print(result2)
