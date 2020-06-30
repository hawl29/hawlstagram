# -*- encoding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.jinja_env.auto_reload = True
app.config.from_pyfile('app.conf')
app.secret_key = 'hawlstagram'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/regloginpage'
from application import views,models
