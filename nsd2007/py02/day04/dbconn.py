from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接数据库的引擎。连不同数据库，关键就在于引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器地址/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu2007?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上输出调试信息，生产环境不要打开
)
Base = declarative_base()  # 生成映射类的基类
Session = sessionmaker(bind=engine)  # 创建到数据库的会话连接类

# 声明映射类
class Department(Base):  # 必须继承于Base
    __tablename__ = 'departments'  # 固定格式，声明该类与哪张表关联
    # 类变量对应字段名，必须是Column的实例
    # 数据库的INT类型，sqlalchemy定义为Integer类
    id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)  # String对应VARCHAR

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
    # 数据库中如果不存在表，则创建；存在则忽略
    Base.metadata.create_all(engine)

