from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接数据库的引擎。连不同数据库，关键就在于引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器地址/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu2007?charset=utf8',
    encoding='utf8',
    echo=True  # 在屏幕上输出调试信息，生产环境不要打开
)
Base = declarative_base()  # 生成映射类的基类
Session = sessionmaker(bind=engine)  # 创建到数据库的会话连接类
