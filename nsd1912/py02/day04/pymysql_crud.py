# Create / Retrieve / Update / Delete
import pymysql

# 建立到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='root', passwd='tedu.cn',
    db='nsd1912', charset='utf8'
)

# 创建游标。游标只是一个术语，类似于文件对象
# 通过文件对象可以实现对文件的读写，通过游标可以实现对数据库的增删改查
cur = conn.cursor()

###################################################################
# 编写sql语句
# insert1 = 'INSERT INTO departments VALUES (%s, %s)'

# 执行sql语句
# cur.execute(insert1, (1, '人事部'))
# cur.executemany(
#     insert1,
#     [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '市场部'), (6, '销售部')]
# )
###################################################################
# 查询语句
# select1 = 'SELECT * FROM departments'
# cur.execute(select1)
#
# result1 = cur.fetchone()  # 取出一行记录
# print(result1)
# print('*' * 30)
# result2 = cur.fetchmany(2)  # 继续取出2行记录
# print(result2)
# print('*' * 30)
# result3 = cur.fetchall()  # 继续取出剩余全部记录
# print(result3)
###################################################################
# 更新操作
# update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
# cur.execute(update1, ('人力资源部', '人事部'))
###################################################################
# 删除
delete1 = 'DELETE FROM departments WHERE dep_id=%s'
cur.execute(delete1, (6,))


# 确认操作
conn.commit()

# 关闭
cur.close()
conn.close()





