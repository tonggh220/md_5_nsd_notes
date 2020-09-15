from datetime import datetime

# 定义9点和12点的时间
t9 = datetime.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = datetime.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

logfile = 'mylog.txt'
with open(logfile) as fobj:
    for line in fobj:
        t = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t >= t12:
            break
        if t >= t9:
            print(line, end='')
