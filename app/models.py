from app import db 

ROLE_USER = 1
ROLE_ADMIN = 0

class User(db.Model):
  user_id = db.Column(db.Integer, primary_key = True)
  user_name = db.Column(db.String(64), index = True, unique = True)
  user_password = db.Column(db.String(64))
  user_email = db.Column(db.String(120), index = True, unique = True)
  user_role = db.Column(db.SmallInteger, default = ROLE_USER)
  user_task = db.relationship('Task', backref='task', lazy='dynamic')

  def __init__(self, user_name, user_password):
    self.user_name = user_name
    self.user_password = user_password

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    return unicode(self.user_id)
    
  def __repr__(self):
    return '<User %r>' % (self.user_name)

class Task(db.Model):
  task_id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
  task_name = db.Column(db.Text, index = True)
  task_description = db.Column(db.Text)
  start_date = db.Column(db.DateTime) 
  end_date = db.Column(db.DateTime)
  task_status_flag = db.Column(db.Integer)

  def __repr__(self):
    return '<task_id %r>' % (self.task_id)

class Label(db.Model):
  label_id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
  Label_name = db.Column(db.Text)
  Label_color = db.Column(db.String(32))

  def __repr__(self):
    return '<label_id %r>' % (self.label_id)

class Task_tags(db.Model):
  task_tag_id = db.Column(db.Integer, primary_key = True)
  task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'))    
  label_id = db.Column(db.Integer, db.ForeignKey('label.label_id'))    
  def __repr__(self):
    return '<label_id %r>' % (self.task_id)