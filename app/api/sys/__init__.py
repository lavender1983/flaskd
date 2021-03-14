#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Project  : flaskd
# File     : __init__.py.py
# Author   : guile
# Version  : v1.0
# Email    : lavender.lhy@gmail.com
# Date     : 2021-03-14 16:34
# Remarks  :
from flask import Blueprint

sys_bp = Blueprint("sys", __name__, url_prefix="/")

from . import routes