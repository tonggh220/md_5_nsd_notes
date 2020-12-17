from dbconn import Session, Department, Employees

# 创建会话实例
session = Session()

# 通过会话实例对数据库增删改查

# 确认
session.commit()

# 关闭会话
session.close()

