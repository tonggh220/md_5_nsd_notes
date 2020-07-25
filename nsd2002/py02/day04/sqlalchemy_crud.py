from sqlalchemy.orm import sessionmaker
from dbconn import engine, Department, Employee, Salary


# 要想实现对数据库的增删改查，首先需要建立到数据库的会话连接
Session = sessionmaker(bind=engine)  # 创建会话类
session = Session()  # 创建会话实例

# 对数据库的CRUD，都是通过session会话实现的
# hr = Department(id=1, name='人事部')
# account = Department(id=2, name='财务部')
# ops = Department(id=3, name='运维部')
# dev = Department(id=4, name='开发部')
# qs = Department(id=5, name='测试部')
# market = Department(id=6, name='市场部')
# sales = Department(id=7, name='销售部')
# 创建一个部门
# session.add(hr)
# 创建多个部门
# session.add_all([account, ops, dev, qs, market, sales])

# 创建员工
# yz = Employee(
#     name='余震', birth_date='1992-1-1',
#     email='yz@tedu.cn', dep_id=1
# )
# zxj = Employee(
#     name='朱晓杰', birth_date='1992-2-15',
#     email='zxj@qq.com', dep_id=2
# )
# mz = Employee(
#     name='毛臻', birth_date='1993-3-10',
#     email='mz@qq.com', dep_id=2
# )
# cpc = Employee(
#     name='谌鹏程', birth_date='1993-4-20',
#     email='cpc@163.com', dep_id=3
# )
# xw = Employee(
#     name='徐武', birth_date='1993-5-4',
#     email='xw@tedu.cn', dep_id=3
# )
# cy = Employee(
#     name='陈煜', birth_date='1995-6-1',
#     email='cy@qq.com', dep_id=4
# )
# plp = Employee(
#     name='彭立平', birth_date='1996-7-1',
#     email='plp@163.com', dep_id=4
# )
# lqc = Employee(
#     name='卢玫呈', birth_date='1996-8-1',
#     email='ljc@163.com', dep_id=4
# )
# yzk = Employee(
#     name='余增科', birth_date='1995-9-30',
#     email='yzk@qq.com', dep_id=5
# )
# lzj = Employee(
#     name='罗正军', birth_date='1995-10-1',
#     email='lzj@qq.com', dep_id=2
# )
# jy = Employee(
#     name='蒋宇', birth_date='1995-11-20',
#     email='jy@qq.com', dep_id=2
# )
# lcf = Employee(
#     name='柳超凡', birth_date='1995-12-25',
#     email='lcf@tedu.cn', dep_id=2
# )
# zw = Employee(
#     name='赵伟', birth_date='1994-1-25',
#     email='zw@tedu.cn', dep_id=3
# )
# session.add_all([yz, zxj, mz, cpc, xw, cy, plp, lqc, yzk, lzj, jy, lcf, zw])

############################################
# 查询
# 把class作为参数，返回的是实例组成的查询集。可以认为查询集就是一个列表
# qset1 = session.query(Department)
# for dep in qset1:
#     # print(dep)
#     print(dep.id, dep.name)
############################################
# 把类变量作为参数，返回的是由元组构成的查询结果
qset2 = session.query(Employee.name, Employee.email)
for data in qset2:
    print(data)

# 对于增删改，务必执行确认操作
session.commit()

# 关闭
session.close()
