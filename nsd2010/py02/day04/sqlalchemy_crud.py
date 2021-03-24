from dbconn import Session, Department, Employee

# 创建会话实例
session = Session()
##################################################
# 通过会话实例对数据库进行增删改查
##################################################
# 增加1个部门
hr = Department(id=1, dep_name='人事部')
session.add(hr)
# 增加多个部门
ops = Department(id=2, dep_name='运维部')
dev = Department(id=3, dep_name='开发部')
qa = Department(id=4, dep_name='测试部')
finance = Department(id=5, dep_name='财务部')
sales = Department(id=6, dep_name='销售部')
market = Department(id=7, dep_name='市场部')
session.add_all([ops, dev, qa, finance, sales, market])

##################################################
# 确认
session.commit()
# 关闭会话
session.close()
