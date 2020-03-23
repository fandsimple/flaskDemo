#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'fandsimple'

    # 是否追踪数据库中数据的改变
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:102487aa@127.0.0.1:3306/firstApp'
    DEBUG = True
    TESTING = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:102487aa@127.0.0.1:3306/firstApp'
    DEBUG = False
    TESTING = True


class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:102487aa@127.0.0.1:3306/firstApp'
    DEBUG = False
    TESTING = False


configDict = {
    'default': DevConfig,
    'dev': DevConfig,
    'test': TestConfig,
    'production': ProductConfig,
}
