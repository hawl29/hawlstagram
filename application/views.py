# -*- encoding:utf-8 -*-

from application import app
from flask import redirect,render_template
from application.models import User,Image,Comment

@app.route('/')
def index():
    images = Image.query.order_by(Image.id.desc()).limit(10).all()
    return render_template('index.html',images=images)

@app.route('/image/<int:image_id>')
def image(image_id):
    image = Image.query.get(image_id)
    if image_id == None:
        return redirect('/') 
    return render_template('pageDetail.html',image = image)

@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = User.query.get(user_id)
    if user == None:
        return redirect('/')
    return render_template('profile.html',user = user)