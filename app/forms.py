from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
  user_name = TextField('user_name', validators = [Required()])
  user_password = TextField('user_password', validators = [Required()])
  remember_me = BooleanField('remeber_me')