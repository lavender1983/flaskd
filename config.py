#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project  : flaskd
# File     : config.py
# Author   : guile
# Version  : v1.0
# Email    : lavender.lhy@gmail.com
# Date     : 2021-03-14 14:27
# Remarks  :
import os
import toml

base_dir = os.path.abspath(os.path.dirname(__name__))
toml_config = toml.load(open(os.path.join(base_dir, "config.toml")))


class Config:
    SECRET_KEY = toml_config.get('SECRET_KEY') or 'hard to guess string'
    POSTS_PER_PAGE = 20
    FOLLOWERS_PER_PAGE = 50
    COMMENTS_PER_PAGE = 30
    SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发环境"""
    Debug = True


class ProductionConfig(Config):
    """生产环境"""


config = {"development": DevelopmentConfig, "production": ProductionConfig, "default": DevelopmentConfig}
