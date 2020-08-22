# create / retrieve / update / delete
import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tedu.cn',
    db='nsd2003',
    charset='utf8mb4',
)

# 创建游标。游标像文件对象一样，通过文件对象对文件读写；通过游标对数据库进行增删改查
cursor = conn.cursor()

############################################
# 编写sql语句
# insert1 = "INSERT INTO departments VALUES(%s, %s)"

# 插入一行数据
# cursor.execute(insert1, (1, '人事部'))
# 插入多行数据
# cursor.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部')])
############################################
# 查询
select1 = "SELECT id, dep_name FROM departments"
cursor.execute(select1)
result1 = cursor.fetchone()  # 取出一行数据
result2 = cursor.fetchmany(2)  # 继续取出2行数据
result3 = cursor.fetchall()  # 继续取出剩余全部数据
print(result1)
print('*' * 30)
print(result2)
print('*' * 30)
print(result3)
############################################
# 确认
conn.commit()
# 关闭
cursor.close()
conn.close()

