# create / retrieve / update / delete

import pymysql

# 创建到服务器的连接
conn = pymysql.connect(
    host='localhost', user='root',
    password='tedu.cn', db='nsd2006', charset='utf8mb4'
)

# 创建游标。游标就像文件对象一样，通过文件对象可以对文件读写，通过游标可以对数据库进行增删改查
cursor = conn.cursor()

####################################
# 编写sql语句
insert1 = "INSERT INTO departments VALUES(%s, %s)"

# 通过游标执行sql语句
# 插入一行数据
cursor.execute(insert1, (1, '人事部'))
# 插入多行数据
cursor.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部')])



####################################
# 如果执行的是增删改操作，需要进行确认
conn.commit()

# 关闭
cursor.close()
conn.close()
