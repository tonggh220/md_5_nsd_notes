from dbconn import Session, Department, Employee

# 创建会话实例
session = Session()
#########################################
# 通过会话实例对数据库进行增删改查



#########################################
# 确认
session.commit()
# 关闭会话连接
session.close()
