from sqlalchemy.orm import sessionmaker
from dbconn import engine, Department, Employee, Salary


# 要想实现对数据库的增删改查，首先需要建立到数据库的会话连接
Session = sessionmaker(bind=engine)  # 创建会话类
session = Session()  # 创建会话实例

# 对数据库的CRUD，都是通过session会话实现的
hr = Department(id=1, name='人事部')
account = Department(id=2, name='财务部')
ops = Department(id=3, name='运维部')
dev = Department(id=4, name='开发部')
qs = Department(id=5, name='测试部')
market = Department(id=6, name='市场部')
sales = Department(id=7, name='销售部')
# 创建一个部门
session.add(hr)
# 创建多个部门
session.add_all([account, ops, dev, qs, market, sales])


# 对于增删改，务必执行确认操作
session.commit()

# 关闭
session.close()
