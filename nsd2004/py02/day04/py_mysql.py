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
create_dep = """CREATE TABLE departments(
id INT, dep_name VARCHAR (20),
PRIMARY KEY(id)
)"""

# 执行sql语句
cur.execute(create_dep)

# 关闭
cur.close()
conn.close()
