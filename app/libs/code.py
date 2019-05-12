# 状态码
class StatusCode:
    # 管理员状态码
    A90000 = {"code":90000,"msg":"操作成功"}
    A90001 = {"code":90001,"msg":"添加用户失败"}
    A90002 = {"code":90002,"msg":"用户名不能为空"}
    A90003 = {"code":90003,"msg":"密码不能为空"}
    A90004 = {"code":90004,"msg":"获取数据失败"}
    A90005 = {"code":90005,"msg":"编辑数据失败"}
    A90006 = {"code":90006,"msg":"删除数据失败"}

    # 角色管理
    A91000 = {"code": 91000, "msg": "成功"}
    A91001 = {"code": 91001, "msg": "删除失败"}
    A91002 = {"code": 91002, "msg": "参数传递有误"}
    A91003 = {"code": 91003, "msg": "该角色绑定其他用户，不能删除"}
    A91004 = {"code": 91004, "msg": "数据插入失败"}
    A91005 = {"code": 91005, "msg": "数据编辑失败"}
    A91006 = {"code": 91006, "msg": "该角色绑定其他用户，不能更新"}

    # 权限管理
    A92000 = {"code": 92000, "msg": "成功"}
    A92001 = {"code": 92001, "msg": "权限添加失败"}
    A92002 = {"code": 92002, "msg": "缺省参数"}
    A92003 = {"code": 92003, "msg": "未获取有效数据"}
    A92004 = {"code": 92004, "msg": "数据编辑失败"}
    A92005 = {"code": 92005, "msg": "数据删除失败"}
    A92006 = {"code": 92006, "msg": "该规则有子节点，不能删除"}