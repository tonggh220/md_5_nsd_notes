import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tedu.cn',
    db='nsd2007',
    charset='utf8mb4'
)

# 创建游标。游标类似于文件对象，通过文件对象可以读写文件，通过游标可以对数据库进行增删改查
cursor = conn.cursor()

# 编写SQL语句
create_dep = """CREATE TABLE departments(
id INT, dep_name VARCHAR (20),
PRIMARY KEY (id)
)"""

# 通过游标执行sql语句
cursor.execute(create_dep)

# 如果是增删改操作，必须执行确认
conn.commit()

# 关闭
cursor.close()
conn.close()




