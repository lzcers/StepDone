from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import User, Task, Label, Task_tags, ROLE_USER, ROLE_ADMIN
from config import TASK_PER_PAGE
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
  if form.validate_on_submit():
    user_name = form.user_name.data
    user_password = form.user_password.data
    remember_me = form.remember_me.data
    remember_me = True if remember_me == 'y' else False
    user = User.query.filter_by(user_name = user_name, user_password = user_password).first()
    if user:
      login_user(user, remember = remember_me)
      return redirect(url_for('home'))
  return render_template('login.html', form = form, app_name = appName, login_faild = True)

@app.route('/logout')
@login_required  
def logout():
  return redirect(url_for('index'))

@app.route('/')
def index():
  appName = 'StepDone'
  form = LoginForm()
  if g.user is not None and g.user.is_authenticated():
    return redirect(url_for('home'))
  return render_template('login.html', form = form, app_name = appName, login_faild = False)

@app.route('/home', methods = ['GET', 'POST'])
@app.route('/home/', methods = ['GET', 'POST'])
@app.route('/home/<int:page>', methods = ['GeT', 'POST'])
@login_required
def home(page = 1):
  user_id = g.user.user_id
  task_list = Task.query.filter_by(user_id = user_id).paginate(page, TASK_PER_PAGE, False)
  user_labels = Label.query.filter_by(user_id = user_id).all() 

  task_id_to_label_id = {}
  for task in task_list.items:
    task_id = task.task_id
    task_tags = Task_tags.query.filter_by(task_id = task_id).all()  
    task_id_to_label_id[task_id] = [tag.label_id for tag in task_tags]
  return render_template('home.html',
                         task_list = task_list,
                         task_id_to_label_id = task_id_to_label_id,
                         user_labels = user_labels)

@app.route('/task/add_task', methods = ['GET', 'POST'])
@login_required
def add_task():
  return render_template('add_task.html')

@app.route('/user/user_info', methods = ['GET', 'POST'])
@login_required
def user_info():
  return render_template('user_info.html')