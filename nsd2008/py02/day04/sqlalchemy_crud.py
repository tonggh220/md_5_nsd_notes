from dbconn import Department, Employees, Session

# 创建到数据库的会话实例
session = Session()
# 通过会话实例进行增删改查


# 确认
session.commit()
# 关闭会话
session.close()
