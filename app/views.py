from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN


@app.route('/')
def index():
  form = LoginForm()
  return render_template('login.html', form = form)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods= ['GET', 'POST'])
@oid.loginhandler
def login():
  form = LoginForm()
  if g.user is not None and g.user.is_authenticated():
    return redirect(url_for('index'))

  if form.validate_on_sumbmit():
    session['remember_me'] = form.remember_me.data
    return oid.try_login(form.user_name.data, ask_for = ['user_name', 'user_password'])
  return render_template('login.html')

# @oid.after_login
# def after_login(resp):
#     if resp.user_name is None or resp.user_name == "":
#         flash('Invalid login. Please try again.')
#         return redirect(url_for('login'))
#     user = User.query.filter_by(user_name = resp.user_name).first()
#     if user is None:
#         nickname = resp.nickname
#         if nickname is None or nickname == "":
#             nickname = resp.email.split('@')[0]
#         user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
#         db.session.add(user)
#         db.session.commit()
#     remember_me = False
#     if 'remember_me' in session:
#         remember_me = session['remember_me']
#         session.pop('remember_me', None)
#     login_user(user, remember = remember_me)
#     return redirect(request.args.get('next') or url_for('index'))


@lm.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))