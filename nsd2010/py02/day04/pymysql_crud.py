# Create / Retrieve / Update / Delete
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
##############################################
# 编写SQL语句
insert1 = 'INSERT INTO departments VALUES (%s, %s)'
# 插入一行记录
cursor.execute(insert1, (1, '人事部'))
# 插入多行记录
cursor.executemany(insert1, [(2, '财务部'), (3, '运维部'), (4, '开发部'), (5, '测试部'), (6, '市场部'), (7, '销售部')])

##############################################
# 确认
conn.commit()
# 关闭
cursor.close()
conn.close()


