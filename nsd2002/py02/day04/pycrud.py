# Create / Retrieve / Update / Delete
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tedu.cn',
    port=3306,
    db='nsd2002',
    charset='utf8mb4'
)
cur = conn.cursor()
#################################
insert1 = 'INSERT INTO employees VALUES (%s, %s, %s)'
# 插入一行数据
cur.execute(insert1, (1, 'tom', 'tom@tedu.cn'))
# 插入多行数据
cur.executemany(insert1, [(2, 'jerry', 'jerry@tedu.cn'), (3, 'jack', 'jack@qq.com'), (4, 'rose', 'rose@163.com')])

#################################
conn.commit()
cur.close()
conn.close()
