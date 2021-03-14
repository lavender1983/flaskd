#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project  : flaskd
# File     : __init__.py.py
# Author   : guile
# Version  : v1.0
# Email    : lavender.lhy@gmail.com
# Date     : 2021-03-14 15:25
# Remarks  :
from flask import Blueprint

main_bp = Blueprint("main", __name__, url_prefix="/api/v1/main")

from . import routes
