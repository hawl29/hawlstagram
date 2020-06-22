# -*- encoding:utf-8 -*-

from application import app

@app.route('/')
def index():
    return 'hello'

