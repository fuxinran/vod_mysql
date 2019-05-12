# 用户控制器
from app.controller import web
from flask import render_template,jsonify,request
from app.models.funcs import insert,select,get_one,update,delete
from app.helper.func_helper import getCurrentTime,to_dict,ajaxReturn,md5,single_to_dict
from app.libs.code import StatusCode

# 读取列表
@web.route('/user')
def user():
    sql = 'select user.id as uid,user.name as name,user.password as password,if(user.status,"启用","锁定") as status,user.addtime as addtime,role.name as rname,role.id as rid from tbl_user as user left join tbl_role as role on user.roleid=role.id;'
    data = select(sql)
    info = to_dict(['id','name','password','status','addtime','rname','rid'],data)
    return render_template('user/index.html',data=info)

# 插入
@web.route('/user/insert',methods=['GET','POST'])
def user_insert():
    if request.method == 'POST':
        name = request.form.get('name').strip() if request.form.get('name') else ''
        if not name:
            return ajaxReturn(StatusCode.A90002)
        password = request.form.get('password').strip() if request.form.get('password') else ''
        if not password:
            return ajaxReturn(StatusCode.A90003)
        roleid = request.form.get('role','0')
        addtime = getCurrentTime(True)
        sql = "insert into tbl_user(`name`,`password`,`addtime`,`roleid`) values(:uname,:password,:addtime,:role)"
        info = [{'uname':name,'password':md5(password),'addtime':addtime,'role':roleid}]
        data = insert(sql,info=info)
        if not data:
            return ajaxReturn(StatusCode.A90001)
        return ajaxReturn(StatusCode.A90000)
    # 获取角色信息
    data = get_role_info()
    return render_template('user/insert.html',data=data)

# 编辑用户
@web.route('/user/update',methods=['GET','POST'])
def user_update():
    if request.method == 'POST':
        code  =request.form.get('code','0')
        status  =request.form.get('status','0')
        role  =request.form.get('role','0')
        sql = "update tbl_user set status={},roleid={} where id={}".format(status,role,code)
        data = update(sql)
        if not data:
            return ajaxReturn(StatusCode.A90005)
        return ajaxReturn(StatusCode.A90000)
    code = request.args.get('code','0')
    sql = "SELECT id,name,status,roleid as rid from tbl_user where id={};".format(code)
    data = get_one(sql)
    if not data:
        return ajaxReturn(StatusCode.A90004)
    info = {}
    roles = get_role_info()
    info['user'] = single_to_dict(['id','name','status','roleid'],data)
    info['roles'] = roles
    return ajaxReturn(StatusCode.A90000,data=info)

@web.route('/user/del')
def user_del():
    code = request.args.get('code',0)
    sql = "delete from tbl_user where id={}".format(code)
    data = delete(sql)
    if not data:
        return ajaxReturn(StatusCode.A90006)
    return ajaxReturn(StatusCode.A90000)


# 获取角色信息
def get_role_info():
    sql = "select id,name from tbl_role where status=1;"
    role = select(sql)
    return to_dict(['id','name'],role)

