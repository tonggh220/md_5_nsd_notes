# 要求取出mylog.txt中
# 2019-05-15 09:00:00~2019-05-15 12:00:00间的日志
import time

# 定义9点和12点的时间
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

dst_fobj = open('/tmp/cutlog.txt', 'w')
with open('mylog.txt') as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t >= t9:
            dst_fobj.write(line)

dst_fobj.close()
