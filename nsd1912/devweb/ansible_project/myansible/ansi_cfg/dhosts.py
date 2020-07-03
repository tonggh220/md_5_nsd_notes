#!/usr/local/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'sqlite:////root/nsd2019/nsd1912/devweb/ansible_project/myansible/db.sqlite3',
    encoding='utf8',  # 字符编码
)

Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50))

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ip_addr = Column(String(15))
    group_id = Column(ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.groupname, Host.ip_addr).join(Host)
    # print(qset.all())
    result = {}
    for g, ip in qset:
        if g not in result:
            result[g] = {}
            result[g]['hosts'] = []
        result[g]['hosts'].append(ip)
    print(result)
