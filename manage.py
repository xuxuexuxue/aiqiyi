import logging

from flask import Flask,session
from flask import Response
from flask import current_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import db, create_app

# 通过指定配置名字创建对应配置的app
app = create_app('development')
# Flask-script添加使用命令行
manager = Manager(app)
# 数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)
#app = Flask(__name__)




if __name__ == '__main__':
    manager.run()
    #app.run()