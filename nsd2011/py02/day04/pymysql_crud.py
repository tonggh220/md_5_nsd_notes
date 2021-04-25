# Create / Retrieve / Update / Delete

import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='tedu.cn',
    db='nsd2011',
    charset='utf8mb4'
)

# 创建游标。游标像文件对象一样，通过文件对象对文件读写；通过游标对数据库进行增删改查
cursor = conn.cursor()

###################################
# 编写sql语句
# insert1 = 'INSERT INTO departments VALUES(%s, %s)'

# 插入一行数据
# cursor.execute(insert1, (1, '人事部'))
# 插入多行数据
# cursor.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部')])
###################################
# 查询
# select1 = 'SELECT * FROM departments'
# cursor.execute(select1)
# result1 = cursor.fetchone()    # 取一行记录
# result2 = cursor.fetchmany(2)  # 继续向后取2行记录
# result3 = cursor.fetchall()    # 继续向后取出全部记录
# print(result1)
# print('*' * 30)
# print(result2)
# print('*' * 30)
# print(result3)
###################################
# 修改
update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
cursor.execute(update1, ('人力资源部', '人事部'))
###################################
# 删除
delete1 = 'DELETE FROM departments WHERE dep_name=%s'
cursor.execute(delete1, ('测试部',))
###################################
# 确认
conn.commit()

# 关闭
cursor.close()
conn.close()
