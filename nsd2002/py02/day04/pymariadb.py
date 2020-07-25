import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tedu.cn',
    port=3306,
    db='nsd2002',
    charset='utf8mb4'
)

# 创建游标。它类似于文件对象，通过文件对象可以对文件进行读写；通过游标可以对数据库进行增删改查
cur = conn.cursor()
# 编写sql语句并执行
create_emp = '''CREATE TABLE employees(
id INT, name VARCHAR (20), email VARCHAR (50),
PRIMARY KEY (id)
)'''
cur.execute(create_emp)
# 如果是增删改，必须commit
conn.commit()
# 关闭游标，关闭到数据库的连接
cur.close()
conn.close()
