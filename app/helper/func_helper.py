from datetime import datetime
import json
import hashlib
# 获取当前时间
def getCurrentTime(flag=False):
    if flag:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return datetime.now()


# 多转成字典
def to_dict(field=[],data=[]):
    info = []
    if not data:
        return info
    for i in data:
        info.append(dict(zip(field, i)))
    return info
# 单转成字典
def single_to_dict(filed=[],data={}):
    if not data:
        return {}
    return dict(zip(filed,data))

# 结构化输出
def ajaxReturn(info={},data={}):
    info['data'] = data
    return json.dumps(info)

# md5加密
def md5(raw):
    md5 = hashlib.md5()
    md5.update(raw.encode('utf8'))
    return  md5.hexdigest()




