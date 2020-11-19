from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器地址/数据库?参数字符串
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu2006?charset=utf8',
    encoding='utf8',
    # echo=True  # 在终端上输出调试信息，生产环境不要使用
)

Base = declarative_base()  # 生成映射类的基类
Session = sessionmaker(bind=engine)  # 创建到数据库的会话连接类

# 创建映射类
class Department(Base):
    __tablename__ = 'departments'  # 固定用法，声明该类与哪张表关联
    id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    birth_date = Column(Date)
    dep_id = Column(Integer, ForeignKey('departments.id'))

if __name__ == '__main__':
    # 如果库中没有相关表则创建，有表则忽略
    Base.metadata.create_all(engine)
