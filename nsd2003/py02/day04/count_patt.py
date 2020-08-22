
def count_patt(fname, patt):
    '用于在fname中统计patt出现的次数'

if __name__ == '__main__':
    fname = 'access_log'
    ip = ''
    br = ''
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
