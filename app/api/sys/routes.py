#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project  : flaskd
# File     : routes.py
# Author   : guile
# Version  : v1.0
# Email    : lavender.lhy@gmail.com
# Date     : 2021-03-14 16:34
# Remarks  :

from . import sys_bp


@sys_bp.route("/ping", methods=["GET"])
def ping():
    return "PONG"
