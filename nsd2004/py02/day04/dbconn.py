from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器地址/数据库?参数字符串
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu2004?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上输出调试信息，生产环境不要打开
)
Session = sessionmaker(bind=engine)  # 创建到数据库的会话连接类
Base = declarative_base()  # 生成映射类的基类

# 声明映射类
class Department(Base):
    __tablename__ = 'departments'  # 固定格式，声明该类与数据库哪张表关联
    id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    birth_date = Column(Date)
    dep_id = Column(Integer, ForeignKey('departments.id'))

class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    # 如果库中无相关的表，则创建；有表则不执行
    Base.metadata.create_all(engine)
