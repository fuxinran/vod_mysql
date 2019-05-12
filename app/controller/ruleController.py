# 规则
from app.controller import web
from flask import request,render_template,jsonify
from app.helper.func_helper import *
from app.models.funcs import *
from app.libs.code import StatusCode

# 规则列表
@web.route('/rule')
def rule():
    sql = "select id,concat(if((length(path)-2),'└',''),concat(repeat('─',(length(path)-2)),name)) as name,src,path,if(status,'启用','禁用') as status,addtime,if(menu,'是','否') as menu,path from tbl_rule where `status`=1 ORDER BY CONCAT(path,id) asc,id desc;"
    data = select(sql)
    info = to_dict(['id','name','src','path','status','addtime','menu','path'],data)
    return render_template('rule/index.html',data=info)

# 添加规则
@web.route('/rule/insert',methods=['GET','POST'])
def rule_insert():
    if request.method == 'POST':
        name = request.form.get('name').strip() if request.form.get('name') else ''
        if not name:
            return ajaxReturn(StatusCode.A92002)
        src = request.form.get('src').strip() if request.form.get('src') else ''
        if not src:
            return ajaxReturn(StatusCode.A92002)
        menu = request.form.get('menu','0')
        pid = request.form.get('pid','0')
        if  pid !='0':
            path = request.form.get('path') + pid + ','
        else:
            path = request.form.get('path','0,')
        addtime = getCurrentTime(True)
        sql = "insert into tbl_rule(`name`,`src`,`pid`,`path`,`menu`,`status`,`addtime`) values(:name,:src,:pid,:path,:menu,:status,:addtime)"
        info = {"name":name,"src":src,"menu":menu,"pid":pid,"path":path,"status":1,"addtime":addtime}
        data = insert(sql,info)
        if not data:
            return ajaxReturn(StatusCode.A92001)
        return ajaxReturn(StatusCode.A92000)
    return render_template('rule/insert.html')

#规则更新
@web.route('/rule/update',methods=['GET','POST'])
def rule_update():
    if request.method == 'POST':
        code = request.form.get('code','0')
        name = request.form.get('name').strip() if request.form.get('name') else ''
        src = request.form.get('src').strip() if request.form.get('src') else ''
        status = request.form.get('status','0')
        menu = request.form.get('menu','0')
        sql = "update tbl_rule set name='{}',src='{}',status={},menu={} where id={}".format(name,src,status,menu,code)
        data = update(sql)
        if not data:
            return ajaxReturn(StatusCode.A92004)
        return ajaxReturn(StatusCode.A92000)
    code = request.args.get('code','0')
    sql = "select id,name,status,src from tbl_rule where id={}".format(code)
    data = get_one(sql)
    if not data:
        return ajaxReturn(StatusCode.A92003)
    info = single_to_dict(['id','name','status','src'],data)
    return ajaxReturn(StatusCode.A92000,data=info)


# 规则删除
@web.route('/rule/del')
def rule_del():
    code = request.args.get('code','0')
    sql = "select count(*) as num from tbl_rule where pid={}".format(code)
    data = get_one(sql)
    if not data:
        return ajaxReturn(StatusCode.A92003)
    if  data[0]:
        return ajaxReturn(StatusCode.A92006)
    sql = "delete from tbl_rule where id={}".format(code)
    data = delete(sql)
    if not data:
        return ajaxReturn(StatusCode.A92005)
    return ajaxReturn(StatusCode.A92000)
