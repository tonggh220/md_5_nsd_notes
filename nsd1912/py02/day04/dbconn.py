from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建到数据库的连接引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器地址/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1912?charset=utf8',
    encoding='utf8',  # 字符编码
    # echo=True  # 运行时，在屏幕上打印调试信息，在生产环境下应该关闭
)

# 创建连接会话类
Session = sessionmaker(bind=engine)
# 创建实体类的基类
Base = declarative_base()

# 声明实体类
class Department(Base):
    __tablename__ = 'departments'  # 定义该class关联哪张表
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

class Employee(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    # 在库中创建表，如果表已存在则略过，不会创建
    Base.metadata.create_all(engine)
