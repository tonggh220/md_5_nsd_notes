import pymysql

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tedu.cn',
    db='nsd2010',
    charset='utf8mb4',
)
# 创建游标。游标就像文件对象一样，通过文件对象可以对文件进行读写，通过游标可以对数据库进行增删改查
cursor = conn.cursor()
# 编写SQL语句
create_dep = '''CREATE TABLE departments(
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR (10)
)'''
# 通过游标执行SQL语句
cursor.execute(create_dep)
# 确认
conn.commit()
# 关闭
cursor.close()
conn.close()

