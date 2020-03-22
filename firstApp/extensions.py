#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_bootstrap import Bootstrap


# 注册插件
def init_app(app):
    # 注册bootstrap插件
    bootstrap = Bootstrap()
    bootstrap.init_app(app)
