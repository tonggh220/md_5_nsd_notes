# create / retrieve / update / delete

import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tedu.cn',
    db='nsd2005',
    charset='utf8mb4',
)

# 创建游标。游标像文件对象一样，通过文件对象对文件读写；通过游标对数据库进行增删改查
cursor = conn.cursor()

############################################
# 编写sql语句
# insert1 = 'INSERT INTO department VALUES (%s, %s)'

# 通过游标执行sql语句
# 插入一行数据
# cursor.execute(insert1, (1, '人事部'))
# cursor.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部')])
############################################
# 查询
select1 = 'SELECT id, dep_name FROM department'
cursor.execute(select1)
result1 = cursor.fetchone()  # 取出一行
result2 = cursor.fetchmany(2)  # 继续取出2行记录
result3 = cursor.fetchall()  # 继续取出剩余全部记录
print(result1)
print('*' * 30)
print(result2)
print('*' * 30)
print(result3)

# 确认
conn.commit()

# 关闭
cursor.close()
conn.close()
