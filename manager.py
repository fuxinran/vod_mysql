# flask 提供的一个外部脚本，通过命令行的方式驱动执行
from flask_script import Manager
# 动态迁移数据库
from flask_migrate import Migrate,MigrateCommand
# 导入app实例
from app import create_app
app = create_app()
# 导入 sqlalchemmy 实例
from app.models import db
# 实例化manger对象
manager = Manager(app=app)
# 实例化 Migrate 对象
migrate = Migrate(app=app,db=db,directory='log/migrations')
# 将migrate对象绑定在manager上
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manager.run()


