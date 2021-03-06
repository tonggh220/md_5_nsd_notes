from dbconn import Department, Employee, Session

# 创建会话实例
session = Session()
###############################
# 通过会话实例对数据库进行增删改查
###############################
# 添加1个部门
# hr = Department(id=1, dep_name='人事部')
# session.add(hr)
# 添加多个部门
# ops = Department(id=2, dep_name='运维部')
# dev = Department(id=3, dep_name='开发部')
# qs = Department(id=4, dep_name='测试部')
# finance = Department(id=5, dep_name='财务部')
# sales = Department(id=6, dep_name='销售部')
# market = Department(id=7, dep_name='市场部')
# session.add_all([ops, dev, qs, finance, sales, market])
###############################
# 新增员工
# lb = Employee(
#     id=1, emp_name='刘备', email='lb@tedu.cn',
#     birth_date='1980-01-01', dep_id=1
# )
# gy = Employee(
#     id=2, emp_name='关羽', email='gy@tedu.cn',
#     birth_date='1981-01-01', dep_id=2
# )
# zf = Employee(
#     id=3, emp_name='张飞', email='zf@tedu.cn',
#     birth_date='1982-01-01', dep_id=2
# )
# zgl = Employee(
#     id=4, emp_name='诸葛亮', email='zgl@qq.com',
#     birth_date='1982-05-04', dep_id=1
# )
# zy = Employee(
#     id=5, emp_name='赵云', email='zy@qq.com',
#     birth_date='1982-06-01', dep_id=3
# )
# hz = Employee(
#     id=6, emp_name='黄忠', email='hz@163.com',
#     birth_date='1975-07-01', dep_id=4
# )
# wy = Employee(
#     id=7, emp_name='魏严', email='wy@163.com',
#     birth_date='1990-08-01', dep_id=5
# )
# session.add_all([lb, gy, zf, zgl, zy, hz, wy])
###############################
# 查询: 如果参数是类名，返回的是实例集
# qset1 = session.query(Department)
# print(qset1)
# for dep in qset1:
#     print(dep.id, dep.dep_name)
# 查询：如果查询的参数是类变量，返回的是由元组构成的查询集
# qset2 = session.query(Employee.emp_name, Employee.email)
# print(qset2)
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
# qset5 = session.query(Department).filter(Department.id>=3, Department.id<=5)
# for dep in qset5:
#     print(dep.id, dep.dep_name)
# 模糊查询
# qset6 = session.query(Employee.emp_name, Employee.email).filter(Employee.email.like('%@tedu.cn'))
# for data in qset6:
#     print(data)
# in
# qset7 = session.query(Department).filter(Department.id.in_([1, 3, 5]))
# for dep in qset7:
#     print(dep.id, dep.dep_name)
# not in
# qset8 = session.query(Department).filter(~Department.id.in_([1, 3, 5]))
# for dep in qset8:
#     print(dep.id, dep.dep_name)
# not null
# qset9 = session.query(Department).filter(Department.dep_name.isnot(None))
# for dep in qset9:
#     print(dep.id, dep.dep_name)
# 多表查询, 参数先写Employee，在join时就要与Department；反过来，道理一样
# qset10 = session.query(Employee.emp_name, Department.dep_name).join(Department)
# for data in qset10:
#     print(data)
###############################
# 取数据时，除了使用for循环，还可以使用all和first方法。
# all取出所有记录，放到列表中，first则只取出第一个结果
# qset11 = session.query(Department.id, Department.dep_name).order_by(Department.id)
# print(qset11.all())
# print(qset11.first())
# 更新
# qset11 = session.query(Department).filter(Department.dep_name=='人事部')
# hr = qset11.first()
# hr.dep_name = '人力资源部'
# 删除
qset12 = session.query(Department).filter(Department.dep_name=='市场部')
market = qset12.first()
session.delete(market)

###############################
# 确认
session.commit()
# 关闭
session.close()
