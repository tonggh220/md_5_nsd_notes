from dbconn import Department, Employees, Session

# 创建到数据库的会话实例
session = Session()
# 通过会话实例进行增删改查
################################
# 增加一个部门
# hr = Department(id=1, dep_name='人事部')
# session.add(hr)
# 增加多个部门
# ops = Department(id=2, dep_name='运维部')
# dev = Department(id=3, dep_name='开发部')
# qa = Department(id=4, dep_name='测试部')
# finance = Department(id=5, dep_name='财务部')
# sales = Department(id=6, dep_name='销售部')
# market = Department(id=7, dep_name='市场部')
# session.add_all([ops, dev, qa, finance, sales, market])
################################
# 新增员工
# lb = Employees(
#     id=1, emp_name='刘备', email='lb@tedu.cn',
#     birth_date='1980-01-01', dep_id=1
# )
# gy = Employees(
#     id=2, emp_name='关羽', email='gy@tedu.cn',
#     birth_date='1981-01-01', dep_id=2
# )
# zf = Employees(
#     id=3, emp_name='张飞', email='zf@tedu.cn',
#     birth_date='1982-01-01', dep_id=2
# )
# zgl = Employees(
#     id=4, emp_name='诸葛亮', email='zgl@qq.com',
#     birth_date='1982-05-04', dep_id=1
# )
# zy = Employees(
#     id=5, emp_name='赵云', email='zy@qq.com',
#     birth_date='1982-06-01', dep_id=3
# )
# hz = Employees(
#     id=6, emp_name='黄忠', email='hz@163.com',
#     birth_date='1975-07-01', dep_id=4
# )
# wy = Employees(
#     id=7, emp_name='魏严', email='wy@163.com',
#     birth_date='1990-08-01', dep_id=5
# )
# session.add_all([lb, gy, zf, zgl, zy, hz, wy])
##################################################
# 查询，如果参数是类名，则返回实例集
# qset1 = session.query(Department)
# print(qset1)  # 此时qset1只是一条sql语句，当向它取值时，才会访问数据库
# for dep in qset1:
#     print(dep.id, dep.dep_name)
#
# 查询，如果参数是字段，则返回由元组构成的查询集
# qset2 = session.query(Employees.emp_name, Employees.email)
# for data in qset2:
#     print(data)

# 排序
# qset3 = session.query(Department).order_by(Department.id)
# for dep in qset3:
#     print(dep.id, dep.dep_name)

# 降序
# qset4 = session.query(Department).order_by(-Department.id)
# for dep in qset4:
#     print(dep.id, dep.dep_name)

# 过滤
# qset5 = session.query(Department)\
#     .filter(Department.id>=3, Department.id<=5)
# for dep in qset5:
#     print(dep.id, dep.dep_name)

# 模糊查询
qset6 = session.query(Employees.emp_name, Employees.email)\
    .filter(Employees.email.like('%@tedu.cn'))
for data in qset6:
    print(data)



###################################
# 确认
session.commit()
# 关闭会话
session.close()
