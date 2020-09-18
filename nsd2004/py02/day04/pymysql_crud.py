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
cur.execute(insert1, (1, '人事部'))
# 插入多行数据
cur.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部')])


# 确认
conn.commit()

# 关闭
cur.close()
conn.close()
