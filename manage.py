# -*- encoding:utf-8 -*-

from application import app,db
from flask_script import Manager
from application.models import User,Image,Comment
import random
manager = Manager(app)

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User'+ str(i),'p'+str(i)))
        for j in range(0,3):
            db.session.add(Image(get_url,i+1))
            for k in range(0,3):
                db.session.add(Comment('conment test'+str(k),3*i+j+1,i+1))
    db.session.commit()

def get_url():
    return 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+ 'm.png'

if __name__ == '__main__':
    manager.run()