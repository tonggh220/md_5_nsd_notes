from dbconn import Department, Employee, Session

# 创建会话实例
session = Session()
####################################
# 通过会实例对数据库进行增删改查等操作
####################################


####################################
# 如果是增删改操作，需要确认
session.commit()
# 关闭
session.close()
