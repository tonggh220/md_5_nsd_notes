from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# 创建连接数据库的引擎
engine = create_engine(
    # mysql+pymsql://用户名:密码@服务器地址/数据库名?参数
    'mysql+pymysql://root:tedu.cn@localhost/tedu2002?charset=utf8',
     encoding='utf8',
     # echo=True  # 在终端上输出调试信息，生产环境需要关闭
)
# 生成映射类的基类
Base = declarative_base()

# 编写映射类
class Department(Base):
    __tablename__ = 'departments'  # 指定数据库中的表名
    id = Column(Integer, primary_key=True)  # Integer -> int
    name = Column(String(20), unique=True)  # String(20) -> varchar(20)

    def __str__(self):
        return "部门<:%s>" % self.name

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    birth_date = Column(Date)
    email = Column(String(50))
    # 配置dep_id与departments表中的id字段是主外键关系
    dep_id = Column(ForeignKey('departments.id'))

    def __str__(self):
        return "<员工:%s>" % self.name

class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(ForeignKey('employees.id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    # 如果数据库中没有相关的表则创建，有的话忽略
    Base.metadata.create_all(engine)
