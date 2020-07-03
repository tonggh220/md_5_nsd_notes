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

# 编写sql语句
create_dep = '''CREATE TABLE departments(
dep_id INT, dep_name VARCHAR (20),
PRIMARY KEY (dep_id)
)'''
create_emp = '''CREATE TABLE employees(
emp_id INT, emp_name VARCHAR (20), birth_date DATE, email INT, dep_id INT,
PRIMARY KEY (emp_id), FOREIGN KEY (dep_id) REFERENCES departments(dep_id)
)'''
create_sal = '''CREATE TABLE salary(
id INT, emp_id INT, date DATE, baisc INT, awards INT,
PRIMARY KEY (id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
)'''

# 执行sql语句
cur.execute(create_dep)
cur.execute(create_emp)
cur.execute(create_sal)

# 确认操作
conn.commit()

# 关闭
cur.close()
conn.close()
