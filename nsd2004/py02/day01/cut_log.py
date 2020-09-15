import time

# 定义9点和12点的时间
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

# 在文件中取每一行，将每一行的时间字符串取出，
# 转成struct_time时间对象，如果是介于9点到12点之间，则打印出来
logfile = 'mylog.txt'
with open(logfile) as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t9 <= t <= t12:
            print(line, end='')
