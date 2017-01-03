# -*- coding:utf-8 -*-
# from datetime import datetime
from flask import render_template,session,redirect,url_for,flash
from . import main
# from .forms import NameForm
from .. import db
from ..models import User
from flask_login import login_required,login_user,logout_user
from ..models import User
from .forms import LoginForm

@main.route('/secret')
@login_required
def secret():
    return '未登录'

@main.route('/',methods=['GET','POST'])
def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         #...
#         return redirect(url_for('.index'))
#     return render_template('index.html',
#                             form=form,name=session.get('name'),
#                             known=session.get('known',False),
#                             current_time=datetime.utcnow())
    return render_template('index.html')
@main.route('/test')
def test():
    return render_template('test.html')

@main.route('/base')
def base():
    return render_template('mybase.html')

@main.route('/login',methods=['GET','POST'])
def login():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user is not None and user.verify_password(form.password.data):
    #         login_user(user,form.remember_me.data)
    #         return redirect(request.args.get('next') or url_for('main.index'))
    #     flash('error')
    # return render_template('main/login.html',form=form)
    return render_template('main/login.html')
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('out')
    return redirect(url_for('main.index'))
