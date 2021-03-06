# -*- encoding:utf-8 -*-

from application import app,db
from flask import redirect,render_template,request,flash,get_flashed_messages
from application.models import User,Image,Comment
import random,hashlib,json
from flask_login import login_required,logout_user,login_user,current_user

@app.route('/')
def index():
    images = Image.query.order_by(Image.id.desc()).paginate(page=1,per_page=5,error_out=False)
    return render_template('index.html',images=images)
@app.route('/index/<int:page>/<int:per_page>/')
def lode_more(page,per_page):
    paginate = Image.query.order_by(Image.id.desc()).paginate(page=page,per_page=per_page,error_out=False)
    map = {'has_next':paginate.has_next}
    images = []
    for image in paginate.items:
        img = {'id':image.id,'url':image.url,'created_time':str(image.created_date),'comment_count':len(image.comments.all()),'user_id':image.user_id,'user_name':image.user.username,'user_head_url':image.user.head_url}
        images.append(img)
    map['images']=images
    return json.dumps(map)

@app.route('/image/<int:image_id>')
def image(image_id):
    image = Image.query.get(image_id)
    if image_id == None:
        return redirect('/') 
    return render_template('pageDetail.html',image = image)

@app.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    user = User.query.get(user_id)
    if user == None:
        return redirect('/')
    image = user.images.paginate(page=1,per_page=3,error_out=False).items
    return render_template('profile.html',user = user,image = image)

@app.route('/profile/images/<int:user_id>/<int:page>/<int:per_page>/')
def user_images(user_id,page,per_page):
    #paginate = user.images.paginate(page=page,per_page=per_page,error_out=False)
    paginate = Image.query.filter_by(user_id=user_id).paginate(page=page,per_page=per_page,error_out=False)
    map = {'has_next':paginate.has_next}
    images = []
    for image in paginate.items:
        img = {'id':image.id,'url':image.url,'comment_count':len(image.comments.all())}
        images.append(img)
    map['images'] = images
    return json.dumps(map)


@app.route('/regloginpage')
def reglogin():
    msg = ''
    for m in get_flashed_messages(with_categories=False,category_filter=['login','reg']):
        msg = msg+m
    return render_template('login.html',msg=msg,next=request.values.get('next'))


def redirect_with_msg(target,msg,cate):
    if msg != None:
        flash(msg,category=cate)
    return redirect(target)

@app.route('/reg/',methods=['GET','POST'])
def reg():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()
    if username == '' or password == '':
        return redirect_with_msg('/regloginpage',u'用户名或密码不能为空','reg')
    user = User.query.filter_by(username = username).first()
    if user != None:
        return redirect_with_msg('/regloginpage',u'用户名已存在','reg')
    #其它判断
    temp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    salt = ''.join(random.sample(temp,10))
    m = hashlib.md5()
    m.update((password+salt).encode('utf-8'))
    password = m.hexdigest()
    db.session.add(User(username,password,salt))
    db.session.commit()
    return redirect('/')

@app.route('/login/',methods=['GET','POST'])
def login():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()
    if username == '' or password == '':
        return redirect_with_msg('/regloginpage',u'用户名或密码不能为空','login')
    user = User.query.filter_by(username=username).first()
    if user == None:
        return redirect_with_msg('/regloginpage',u'用户不存在','login')
    m = hashlib.md5()
    m.update((password+user.salt).encode('utf-8'))    
    if m.hexdigest() != user.password:
        return redirect_with_msg('/regloginpage',u'密码错误','login')
    login_user(user)
    next = request.values.get("next")
    if next != None and next.startswith('/'):
        return redirect(next)
    return redirect('/')



@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')



