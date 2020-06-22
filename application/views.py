# -*- encoding:utf-8 -*-

from hawlstagram import app

@app.route('/')
def index():
    return 'hello'

