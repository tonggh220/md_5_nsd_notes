from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/myansible2?charset=utf8',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)
