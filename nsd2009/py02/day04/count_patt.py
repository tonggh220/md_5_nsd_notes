
def count_patt(fname, patt):

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.0.2345.29  192.168.1.25
    br = 'Chrome|Firefox|MSIE'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
