from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm, TaskForm
from models import User, Task, Label, Task_tags, ROLE_USER, ROLE_ADMIN
from config import TASK_PER_PAGE
from datetime import datetime

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
  logout_user()
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
@app.route('/home/<int:page>', methods = ['GET', 'POST'])
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
  form = TaskForm()
  if request.method == 'POST':
    if form.validate_on_submit():
      task_name = form.task_name.data
      start_date = form.start_date.data
      end_date = form.end_date.data
      form_task = form.form_serialize()
      form_task['user_id'] = g.user.user_id
      task = Task(form_task)  
      db.session.add(task)
      db.session.commit()
    else:
      return "submit faild"
  return render_template('add_task.html', form = form)

@app.route('/user/user_info', methods = ['GET', 'POST'])
@login_required
def user_info():
  return render_template('user_info.html')

@app.route('/task/del_task', methods = ['POST'])
@login_required
def del_task():
  task = Task.query.get(request.form['task_id'])
  db.session.delete(task)
  db.session.commit()
  return '1'

@app.route('/task/edit_task/<task_id>', methods = ['GET', 'POST'])
@login_required
def task_edit(task_id):
  form = TaskForm()
  task = Task.query.get(task_id)
  if request.method == 'GET':
    return render_template('edit_task.html', form = form, task = task)
  elif request.method == 'POST':
    if form.validate_on_submit():
      format = "%Y-%m-%d" 
      task.task_name = form.task_name.data
      task.start_date = datetime.strptime(form.start_date.data, format)
      task.end_date = datetime.strptime(form.end_date.data, format)
      db.session.commit()
    return 'test'

@app.route('/task/finish_task/<task_id>', methods = ['GET', 'POST'])
@login_required
def task_finish(task_id):
  task = Task.query.get(task_id)
  task.task_status_flag = 1
  db.session.commit()
  return str(task.task_status_flag)