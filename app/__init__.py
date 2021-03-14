#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project  : flaskd
# File     : __init__.py.py
# Author   : guile
# Version  : v1.0
# Email    : lavender.lhy@gmail.com
# Date     : 2021-03-14 14:27
# Remarks  :
from flask import Flask

from app.extensions import socketio
from config import config


def create_app(config_name):
    """
    创建flask app
    Args:
        config_name: 配置名称

    Returns:

    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 注册组件
    _register_extensions(app)
    # 注册蓝图
    _register_blueprint(app)

    return app


def _register_extensions(app):
    """
    注册组件
    Args:
        app:

    Returns:

    """
    socketio.init_app(app)


def _register_blueprint(app):
    """
    注册蓝图
    Args:
        app:

    Returns:

    """
    from app.api.sys import sys_bp
    app.register_blueprint(sys_bp)

    from app.api.v1.main import main_bp
    app.register_blueprint(main_bp)
