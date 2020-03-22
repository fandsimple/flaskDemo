#!/usr/bin/python
# -*- coding: utf-8 -*-

from .main import main

blueprint_config = [
    (main, ''),
]


# 蓝图注册
def register_blueprint(app):
    for blueprintName, prefix in blueprint_config:
        app.register_blueprint(blueprintName, url_prefix=prefix)

