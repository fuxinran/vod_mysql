# 角色管理
from app.controller import web
from app.models.funcs import *
from app.helper.func_helper import *
from flask import request,render_template,jsonify
from app.libs.code import StatusCode

# 角色列表
@web.route('/role')
def role():
    sql = 'select id as rid,name as rname,if(status,"启用","禁用") as status,addtime as addtime from tbl_role'
    data = select(sql)
    info = to_dict(['rid', 'rname', 'status', 'addtime'], data)
    return render_template('role/index.html', data=info)


# 角色添加
@web.route('/role/insert',methods=['GET','POST'])
def role_insert():
    if request.method == 'POST':
        name = request.form.get('name').strip() if request.form.get('name') else ''
        if not name:
            return ajaxReturn()
        sql = "insert into tbl_role(`name`,`addtime`,`status`) values(:name,:addtime,:status)"
        info = {"name":name,"addtime":getCurrentTime(True),"status":1}
        data = insert(sql,info)
        if not data:
            return ajaxReturn(StatusCode.A91004)
        else:
            return ajaxReturn(StatusCode.A91000)
    return render_template('role/insert.html')

# 角色编辑
@web.route('/role/update',methods=['GET','POST'])
def role_update():
    if request.method == 'POST':
        code = request.form.get("code",'0')
        if not code:
            return ajaxReturn(StatusCode.A91002)
        sql = "select count(*) as num from tbl_user where roleid={}".format(code)
        data = get_one(sql)
        if data[0]:
            return ajaxReturn(StatusCode.A91006)
        status = request.form.get("status","0")
        sql = "update tbl_role set status={} where id={}".format(status,code)
        data = update(sql)
        if not data:
            return ajaxReturn(StatusCode.A91005)
        return ajaxReturn(StatusCode.A91000)
    code = request.args.get('code','0')
    sql = "select id,name,status from tbl_role where id={}".format(code)
    data = get_one(sql)
    info = single_to_dict(['id','name','status'],data)
    return ajaxReturn(StatusCode.A91000,data=info)

# 角色删除
@web.route('/role/del')
def role_del():
    code = request.args.get('code','0')
    if not code:
        return ajaxReturn(StatusCode.A91002)
    sql = "select count(user.id) as num from tbl_role as role left join tbl_user as user on user.roleid=role.id where role.id={}".format(code)
    data = get_one(sql)
    if data[0]:
        return ajaxReturn(StatusCode.A91003)
    sql = "delete from tbl_role where id="+code
    data = delete(sql)
    if not data:
        return ajaxReturn(StatusCode.A91001)
    return ajaxReturn(StatusCode.A91000)

# 角色授权
@web.route('/role/auth',methods=['GET','POST'])
def role_auth():
    if request.method == 'POST':
        code = request.form.get('code',0)
        sql = "delete from tbl_rule_role where roleid={}".format(code)
        delete(sql)
        auth = request.values.getlist('name[]')
        if auth:
            info = []
            for i in auth:
                info.append({'roleid':code,'ruleid':i})
            sql = "insert into tbl_rule_role(`roleid`,`ruleid`)values(:roleid,:ruleid)"
            data = insert(sql,info)
            if not data:
                return ajaxReturn(StatusCode.A91007)
        return ajaxReturn(StatusCode.A91000)
    code = request.args.get('code','0')
    sql = "select rule.id,if(length(rule.path)>2,concat('└',repeat('─',(length(path)-2)),rule.name),rule.name) as name,r.roleid as roleid from tbl_rule as rule LEFT JOIN tbl_rule_role as r on r.ruleid = rule.id group by concat(rule.path,rule.id) asc;"
    data = select(sql)
    info = to_dict(['rid','name','roleid'],data)
    print(info)
    return render_template('role/auth.html',data=info,code=code)

# # 获取所有权限
# def get_all_rule():
#     sql = "select * from "
#     return ''