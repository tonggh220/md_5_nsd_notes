from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 创建连接数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器地址/数据库?参数字符串
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu2003?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上输出调试信息，生产环境不要打开
)
Base = declarative_base()  # 生成映射类的基类

# 声明映射类
class Department(Base):
    __tablename__ = 'departments'  # 固定名称，声明该类与哪张表关联
    id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

if __name__ == '__main__':
    # 如果库中无表则创建，有表则不执行
    Base.metadata.create_all(engine)
