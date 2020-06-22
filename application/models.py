# -*- encoding:utf-8 -*-

from application import db
import random
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    
    image = db.relationship('Image')
    comments = db.relationship('Comment')

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.head_url = 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+ 'm.png'

    def __repr__(self):
        return '<User %d %s>' % (self.id,self.username)

class Image(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    url = db.Column(db.String(512))
    created_date = db.Column(db.DateTime)

    User = db.relationship('User')
    comments = db.relationship('Comment')

    def __init__(self,url,user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime.now()
    def __repr__(self):
        return '<Image %d %s>' % (self.id,self.url)

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.String(1024))
    image_id = db.Column(db.Integer,db.ForeignKey('image.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    status = db.Column(db.Integer,default=0)

    user = db.relationship('User')
    image = db.relationship('Image')
    
    def __init__(self,content,image_id,user_id):
        self.image_id = image_id
        self.user_id = user_id
        self.content = content

    def __repr__():
        return '<Comment %d %s>' % (self.id,self.content)