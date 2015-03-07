from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(userid):
    return User.query.get(int(userid))
    
@app.before_request
def before_request():
    g.user = current_user

@app.route('/login', methods= ['POST'])
def login():
  form = LoginForm()
  appName = 'StepDone'
  user_name = form.user_name.data
  user_password = form.user_password.data
  remember_me = form.remember_me.data
  remember_me = True if remember_me == 'y' else False

  if form.validate_on_submit():
    user = User.query.filter_by(user_name = user_name, user_password = user_password).first()
    if user:
      login_user(user, remember = remember_me)
      return redirect(url_for('home'))
  return render_template('login.html', form = form, app_name = appName, login_faild = True)

@app.route('/logout')
@login_required  
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/')
def index():
  appName = 'StepDone'
  form = LoginForm()
  if g.user is not None and g.user.is_authenticated():
    return redirect(url_for('home'))
  return render_template('login.html', form = form, app_name = appName, login_faild = False)

@app.route('/home')
@login_required
def home():
  return render_template('home.html')