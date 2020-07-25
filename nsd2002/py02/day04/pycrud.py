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
# insert1 = 'INSERT INTO employees VALUES (%s, %s, %s)'
# 插入一行数据
# cur.execute(insert1, (1, 'tom', 'tom@tedu.cn'))
# 插入多行数据
# cur.executemany(insert1, [(2, 'jerry', 'jerry@tedu.cn'), (3, 'jack', 'jack@qq.com'), (4, 'rose', 'rose@163.com')])

# 查询
# select1 = 'SELECT id, name, email FROM employees'
# cur.execute(select1)
# result1 = cur.fetchone()    # 取出一个记录
# result2 = cur.fetchmany(2)  # 继续取出2个记录
# result3 = cur.fetchall()    # 取出剩余全部记录
# print(result1)
# print('*' * 30)
# print(result2)
# print('*' * 30)
# print(result3)

# 更新
# update1 = 'UPDATE employees SET email=%s WHERE name=%s'
# cur.execute(update1, ('tom@tarena.com', 'tom'))

# 删除
delete1 = 'DELETE FROM employees WHERE id=%s'
cur.execute(delete1, (4,))

#################################
conn.commit()
cur.close()
conn.close()
