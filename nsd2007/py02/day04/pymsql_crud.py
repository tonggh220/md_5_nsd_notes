# create / retrieve / update / delete
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

# 编写SQL语句, 新增记录
insert1 = "INSERT INTO departments VALUES(%s, %s)"

# 新增一个部门
cursor.execute(insert1, (1, '人事部'))

# 增加多个部门
deps = [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部')]
cursor.executemany(insert1, deps)

# 如果是增删改操作，必须执行确认
conn.commit()

# 关闭
cursor.close()
conn.close()
