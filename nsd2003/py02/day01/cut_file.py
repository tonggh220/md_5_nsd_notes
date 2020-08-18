import time

logfile = 'mylog.txt'
# 定义9点和12点的9元组时间
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

with open(logfile) as fobj:
    for line in fobj:
        # 取出一行中的前19个字符，并转成9元组时间
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t9 <= t < t12:
            print(line, end='')
