from dbconn import Session, Department, Employee

# 创建到达数据库的会话实例
session = Session()

# 创建部门
# hr = Department(dep_id=1, dep_name='人事部')
# ops = Department(dep_id=2, dep_name='运维部')
# dev = Department(dep_id=3, dep_name='开发部')
# qa = Department(dep_id=4, dep_name='测试部')
# market = Department(dep_id=5, dep_name='市场部')
# sales = Department(dep_id=6, dep_name='销售部')
# session.add(hr)
# session.add_all([ops, dev, qa, market, sales])

# 添加员工
# ljh = Employee(
#     emp_id=1, emp_name='李家豪',
#     birth_date='1995-1-1', email='ljh@tedu.cn', dep_id=1
# )
# ly = Employee(
#     emp_id=2, emp_name='罗杨',
#     birth_date='1998-1-15', email='ly@qq.com', dep_id=2
# )
# lhy = Employee(
#     emp_id=3, emp_name='李瀚阳',
#     birth_date='1997-5-1', email='lhy@163.com', dep_id=2
# )
# xl = Employee(
#     emp_id=4, emp_name='肖龙',
#     birth_date='1996-5-4', email='xl@tedu.cn', dep_id=3
# )
# jyf = Employee(
#     emp_id=5, emp_name='蒋益丰',
#     birth_date='1997-6-1', email='jyf@qq.com', dep_id=4
# )
# hxy = Employee(
#     emp_id=6, emp_name='侯岫钰',
#     birth_date='2000-8-1', email='hxy@tedu.cn', dep_id=5
# )
# session.add_all([ljh, ly, lhy, xl, jyf, hxy])
########################################
# 查询时，传入的参数是类，返回的是实例集合
# qset1 = session.query(Department)
# print(qset1)  # 只是一个sql语句，只有向它取值时，才会真正的连接数据库
# print(qset1.all())  # all方法返回列表
# for dep in qset1:   # 也可以通过for循环取值
#     print(dep.dep_id, dep.dep_name)
########################################
# 查询时，传入的参数是属性，返回的是由属性构成的元组的集合
# qset2 = session.query(Employee.emp_name, Employee.email)
# print(qset2.all())
# for data in qset2:
#     print(data)
########################################
# 排序
# qset3 = session.query(Department).order_by(Department.dep_id)
# for dep in qset3:
#     print(dep.dep_id, dep.dep_name)
########################################
# 过滤
# qset4 = session.query(Department).filter(Department.dep_name=='人事部')
# for dep in qset4:
#     print(dep.dep_id, dep.dep_name)

# qset5 = session.query(Department).filter(Department.dep_id > 3)
# for dep in qset5:
#     print(dep.dep_id, dep.dep_name)

########################################
# filter可以嵌套多层
# qset6 = session.query(Department).filter(Department.dep_id > 2).filter(Department.dep_id < 5)
# for dep in qset6:
#     print(dep.dep_id, dep.dep_name)
########################################
#
# qset7 = session.query(Employee.emp_name, Employee.email).filter(Employee.email.like('%com'))
# for data in qset7:
#     print(data)
########################################
# 1、3、5号部门
# qset8 = session.query(Department).filter(Department.dep_id.in_([1, 3, 5]))
# for dep in qset8:
#     print(dep.dep_id, dep.dep_name)
########################################
# 非1、3、5号部门
# qset9 = session.query(Department).filter(~Department.dep_id.in_([1, 3, 5]))
# for dep in qset9:
#     print(dep.dep_id, dep.dep_name)

########################################
# 多表查询 query时先写Employee，join时写Department；反之亦然
# qset10 = session.query(Employee.emp_name, Department.dep_name).join(Department)
# for data in qset10:
#     print(data)

# qset11 = session.query(Department.dep_name, Employee.emp_name).join(Employee)
# for data in qset11:
#     print(data)
########################################
# 查询后，可以用循环取值，也可以使用all和first方法取值。
# all是取出全部数据，保存到列表中，first是取出第一个满足条件的数据
# qset12 = session.query(Department).filter(Department.dep_id < 3)
# print(qset12.all())
# print(qset12.first())
########################################
# 更新
# qset13 = session.query(Department).filter(Department.dep_name == '人事部')
# hr = qset13.first()
# hr.dep_name = '人力资源部'
########################################
# 删除
qset14 = session.query(Department).filter(Department.dep_id == 6)
sales = qset14.first()
session.delete(sales)

# 确认
session.commit()

# 关闭
session.close()
