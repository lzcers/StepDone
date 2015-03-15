from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    user_name = TextField('user_name', validators = [DataRequired()])
    user_password = TextField('user_password', validators = [DataRequired()])
    remember_me = BooleanField('remeber_me')

class TaskForm(Form):
    task_name = TextField('task_name', validators = [DataRequired()])
    start_date = TextField('start_date', validators = [DataRequired()])
    end_date = TextField('end_date', validators = [DataRequired()])
    
    def form_serialize(self):
        form_task = {}
        form_task['task_name'] = self.task_name.data
        form_task['start_date'] = self.start_date.data
        form_task['end_date'] = self.end_date.data
        return form_task


