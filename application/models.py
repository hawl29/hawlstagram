# -*- encoding:utf-8 -*-

from application import db,login_manager
import random
from datetime import datetime

class Image(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    url = db.Column(db.String(512))
    created_date = db.Column(db.DateTime)

    #lazy指定的是image到comments的访问方式，dynamic将返回一个query对象
    #selcet返回包含查询结果的list
    comments = db.relationship('Comment',backref='image',lazy='dynamic')

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

    #user = db.relationship('User')
    #image = db.relationship('Image')
    
    def __init__(self,content,image_id,user_id):
        self.image_id = image_id
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return '<Comment %d %s>' % (self.id,self.content)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    salt = db.Column(db.String(12))
    #设置backref，使得image中也有指向user的关系。
    images = db.relationship('Image',backref='user',lazy='dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')

    def __init__(self,username,password,salt=''):
        self.username = username
        self.password = password
        self.head_url = 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+ 'm.png'
        self.salt = salt
    def __repr__(self):
        return '<User %d %s>' % (self.id,self.username)

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)