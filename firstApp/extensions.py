#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()


# 注册插件
def init_app(app):
    # 注册bootstrap插件
    bootstrap.init_app(app)

    # 注册sqlalchemy
    db.init_app(app)
