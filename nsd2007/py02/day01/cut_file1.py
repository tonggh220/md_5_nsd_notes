import time

# 定义9点和12点的时间
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

# 取出文件的每一行的时间，如果时间介于9点和12点之间，就输出
with open('mylog.txt') as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        # if t9 <= t <= t12:
        #     print(line, end='')
        if t > t12:
            break
        if t >= t9:
            print(line, end='')
