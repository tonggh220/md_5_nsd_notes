#!/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/myansible?charset=utf8',
     encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50))

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ip_addr = Column(String(11))
    group_id = Column(Integer, ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.groupname, Host.ip_addr).join(Host)
    # print(qset.all())
    result = {}
    for g, ip in qset:
        if g not in result:  # 组不在字典中，新建项目
            result[g] = {}
            result[g]['hosts'] = []
        result[g]['hosts'].append(ip)  # 把ip地址追加到列中
    print(result)
