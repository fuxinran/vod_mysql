# flask核心文件
from flask import Flask

# 生成app实例
def create_app():
    # 实例化Flask 获得app实例
    app = Flask(__name__,template_folder='views')
    # 注册蓝图
    register_blueprint(app)
    # 注册配置文件
    register_configure(app)
    # 注册数据库
    register_database(app)
    # 注册全文搜索
    register_fulltext(app)
    return app

# 注册蓝图
def register_blueprint(app):
    from app.controller import web
    app.register_blueprint(web)

# 注册配置文件
def register_configure(app):
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

# 注册数据库
def register_database(app):
    from app.models import db
    db.init_app(app)

# 注册全文搜索
def register_fulltext(app):
    import flask_whooshalchemyplus
    flask_whooshalchemyplus.init_app(app=app)