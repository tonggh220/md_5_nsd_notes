# Create / Retrieve / Update / Delete
import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tedu.cn',
    db='nsd2004',
    charset='utf8mb4',
)

# 创建游标。游标像文件对象一样，通过文件对象对文件读写；通过游标对数据库进行增删改查
cur = conn.cursor()

# 编写sql语句
insert1 = "INSERT INTO departments VALUES(%s, %s)"

# 插入一行数据
# cur.execute(insert1, (1, '人事部'))
# 插入多行数据
# cur.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部')])
##########################################
# 查询
# select1 = "SELECT id, dep_name FROM departments"
# cur.execute(select1)
# result1 = cur.fetchone()  # 取出一行数据
# result2 = cur.fetchmany(2)  # 继续取出2行数据
# result3 = cur.fetchall()  # 继续取出剩余全部数据
# print(result1)
# print('*' * 30)
# print(result2)
# print('*' * 30)
# print(result3)
##########################################
# 修改
# update1 = "UPDATE departments SET dep_name=%s WHERE dep_name=%s"
# cur.execute(update1, ("人力资源部", "人事部"))
# select2 = "SELECT id, dep_name FROM departments WHERE dep_name=%s"
# cur.execute(select2, ("人力资源部",))
# print(cur.fetchall())
##########################################
# 删除
delete1 = "DELETE FROM departments WHERE id=%s"
cur.execute(delete1, (5,))

# 确认
conn.commit()

# 关闭
cur.close()
conn.close()
