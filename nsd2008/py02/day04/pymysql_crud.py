# 增加(Create)、检索(Retrieve)、更新(Update)和删除(Delete)

import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tedu.cn',
    db='nsd2008',
    charset='utf8mb4',
)

# 创建游标。游标像文件对象一样，通过文件对象对文件读写；
# 通过游标对数据库进行增删改查
cursor = conn.cursor()

##############################
# 插入语句
# insert1 = "INSERT INTO departments VALUES (%s, %s)"
# # 插入一行数据
# cursor.execute(insert1, (1, '人事部'))
# # 插入多行数据
# cursor.executemany(
#     insert1,
#     [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部')]
# )
##############################
# 查询
select1 = "SELECT * FROM departments ORDER BY id"
cursor.execute(select1)
result1 = cursor.fetchone()  # 取出一行
print(result1)
print('*' * 30)
result2 = cursor.fetchmany(2)  # 继续取出2行
print(result2)
print('*' * 30)
result3 = cursor.fetchall()  # 继续向后取出所有行
print(result3)

##############################
# 确认
conn.commit()

# 关闭
cursor.close()
conn.close()
