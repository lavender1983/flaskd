#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project  : flaskd
# File     : routes.py
# Author   : guile
# Version  : v1.0
# Email    : lavender.lhy@gmail.com
# Date     : 2021-03-14 15:25
# Remarks  :
import time

from flask import jsonify, render_template, session, copy_current_request_context
from . import main_bp
from flask_socketio import emit, disconnect
from app.extensions import socketio


@main_bp.route("/todo/<int:id>", methods=["GET"])
def todo_item(id):
    return jsonify({"task": "Say: 'Hello World!'"})


@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html", async_mode=None)


@main_bp.route("sleep", methods=["GET"])
def sleep():
    time.sleep(20)
    return jsonify({"task": "finished!"})


@socketio.event
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': message['data'], 'count': session['receive_count']})


@socketio.event
def disconnect_request():

    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    # for this emit we use a callback function
    # when the callback function is invoked we know that the message has been
    # received and it is safe to disconnect
    emit('my_response', {'data': 'Disconnected!', 'count': session['receive_count']}, callback=can_disconnect)
