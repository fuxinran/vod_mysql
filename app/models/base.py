from app.models import db
from sqlalchemy import Column,String,Integer,Text,DateTime,SmallInteger
from app.helper.func_helper import getCurrentTime

# 管理员
class User(db.Model):
    __tablename__ = 'tbl_user'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(32),default='',unique=True)
    password = Column(String(128),nullable=False)
    status = Column(SmallInteger,default=1)
    roleid = Column(Integer,db.ForeignKey('tbl_role.id'))
    addtime = Column(DateTime,default=getCurrentTime)
    __table_args__ ={
        'mysql_charset': 'utf8'
    }

# 权限规则表
rule_role = db.Table(
    'tbl_rule_role',
    Column('id',Integer,autoincrement=True,primary_key=True),
    Column('roleid',Integer,db.ForeignKey('tbl_role.id')),
    Column('ruleid',Integer,db.ForeignKey('tbl_rule.id')),
)

# 角色
class Role(db.Model):
    __tablename__ = 'tbl_role'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(32), default='', unique=True)
    status = Column(SmallInteger, default=1)
    addtime = Column(DateTime, default=getCurrentTime)
    users = db.relationship('User',backref=db.backref('roles'))
    rules = db.relationship('Rule',backref=db.backref('roles'),secondary=rule_role)
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

# 规则/权限
class Rule(db.Model):
    __tablename__ = 'tbl_rule'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(32), default='', unique=True)
    # 路由
    src = Column(String(128),default='')
    # 父id
    pid = Column(Integer,default=0)
    # id和父id的关系
    path = Column(String(128),default='0,')
    # 是否是菜单 0 否 1 是
    menu = Column(SmallInteger,default=0)
    status = Column(SmallInteger, default=1)
    addtime = Column(DateTime, default=getCurrentTime)
    __table_args__ = {
        'mysql_charset': 'utf8'
    }