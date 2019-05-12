# 模型方法
from app.models.base import db

# 插入支持批量插入
'''
sql预格式化处理，防止sql注入
sql语句：insert into 表名(`字段1`,`字段2`) values(:字段1,:字段2)
数据 [{'字段1':'值1','字段2':'值2'}]
'''
def insert(sql,info=[]):
    try:
        if not info:
            return 0
        data = db.session.execute(sql,info)
        db.session.commit()
        return data.rowcount
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0

# 查询
def select(sql):
    try:
        return db.session.execute(sql).fetchall()
    except Exception as e:
        return []

# 查询一条数据
def get_one(sql):
    try:
         return db.session.execute(sql).fetchone()
    except:
        return {}

# 编辑
def update(sql):
    try:
        data = db.session.execute(sql)
        db.session.commit()
        return data.rowcount
    except Exception as e:
        db.session.rollback()
        return 0

#删除
def delete(sql):
    try:
        data = db.session.execute(sql)
        db.session.commit()
        return data.rowcount
    except:
        db.session.rollback()
        return 0


