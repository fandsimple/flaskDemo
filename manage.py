#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_migrate import MigrateCommand
from flask_script import Manager
from firstApp import create_app

# 创建app
app = create_app()

# flask-script命令行管理插件
manager = Manager(app=app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
