from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
  user_name = TextField('user_name', validators = [DataRequired()])
  user_password = TextField('user_password', validators = [DataRequired()])
  remember_me = BooleanField('remeber_me')