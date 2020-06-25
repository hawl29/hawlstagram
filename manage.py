# -*- encoding:utf-8 -*-

from application import app,db
from flask_script import Manager
from application.models import User,Image,Comment
from sqlalchemy import or_,and_,func
import random
manager = Manager(app)

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User'+ str(i+1),'p'+str(i)))
        for j in range(0,3):
            db.session.add(Image(get_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('conment test'+str(k),3*i+j+1,i+1))
    db.session.commit()

@manager.command
def query_test():
    #print(1,User.query.all())
    #print(2,User.query.get(3))
    #print(3,User.query.filter_by(id=5).all())
    #print(4,User.query.order_by(User.id.desc()).offset(1).limit(2).all())
    #print(5,User.query.filter(User.username.endswith('0')).limit(2).all())
    #print(6,User.query.filter(or_(User.id == 88,User.id==99)).all())
    #print(7,User.query.paginate(page=4,per_page=10).items)
    
    #通过在model中设置relationship,可以直接通过类中的属性访问关联的信息。
    #user = User.query.get(1)
    #print(user.images)

    #image = Image.query.get(1)
    #comment = Comment.query.get(2)
    #print(comment.user,comment.image)
    
    #两种更新方式：
    #for i in range(50,100,2):
    #    u = User.query.get(i)
    #    u.username = '[NEW]' + u.username
    #
    #User.query.filter(User.id > 50).update({'password':'123'})
    #db.session.commit()
   
    #删除
    #for i in range(50,100,2):
    #    c = Comment.query.get(i+1)
    #    db.session.delete(c)
    #db.session.commit()
    #
    #Comment.query.filter_by(id=3).delete()
    #db.session.commit()
    
    #print(1,User.query.filter_by(id=1).all())
    #print(2,User.query.get(1))
    #print(3,User.query.order_by(User.id.desc()).all())
    #print(4,Image.query.group_by(Image.user_id))
    #print(5,User.query.filter(User.username.endswith('2')).all())
    #print(6,User.query.filter(or_(User.id>=90,User.id<=30)).paginate(page=1,per_page=10).items)

    #u = User.query.get(4)
    #print(u.images[1].url)

    #u = User.query.get(1)
    #u.username = 'hawl'
    #db.session.commit()

    #User.query.filter_by(id=1).update({'username':'sophie'})
    #db.session.commit()
    
    #Comment.query.filter_by(id=1).delete()
    #db.session.commit()
    #c= Comment.query.get(2)
    #db.session.delete(c)
    #db.session.commit()

    #db.session.add(Comment('conmment test 0',1,1))
    #db.session.commit()

    print(Image.query.order_by(Image.id.desc()).limit(10).all())

def get_url():
    return 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+ 'm.png'


if __name__ == '__main__':
    manager.run()