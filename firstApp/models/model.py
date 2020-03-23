#!/usr/bin/python
# -*- coding: utf-8 -*-


from .baseModel import BaseModel
from firstApp.extensions import db
from datetime import datetime


# User 模型类
class UserModel(db.Model, BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 自增ID
    username = db.Column(db.String(12), index=True, unique=True)  # 用户名
    password_hash = db.Column(db.String(128))  # 密码 密文
    sex = db.Column(db.Boolean, default=True)  # 性别
    age = db.Column(db.Integer, default=18)  # 年龄 默认18
    email = db.Column(db.String(50), unique=True)  # 邮箱
    icon = db.Column(db.String(70), default='default.png')  # 头像 默认为default.jpg
    lastLogin = db.Column(db.DateTime)  # 上次登录时间
    registerTime = db.Column(db.DateTime, default=datetime.utcnow)  # 注册时间
    confirm = db.Column(db.Boolean, default=False)  # 激活状态 默认未激活（需要发送邮件进行激活）


# python manage.py db init 初始化
# python manage.py db migrate 生成迁移文件
# python manage.py db upgrade 更新数据库