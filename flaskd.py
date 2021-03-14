#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project  : flaskd
# File     : flaskd.py
# Author   : guile
# Version  : v1.0
# Email    : lavender.lhy@gmail.com
# Date     : 2021-03-14 14:00
# Remarks  :
import eventlet

eventlet.monkey_patch()

import os

from app import create_app
from app.extensions import socketio

app = create_app(os.getenv("FLASK_ENV") or "default")

if __name__ == '__main__':
    socketio.run(app)
