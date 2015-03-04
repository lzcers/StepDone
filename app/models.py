from app import db 

ROLE_USER = 1
ROLE_ADMIN = 0

class User(db.Model):
  user_id = db.Column(db.Integer, primary_key = True)
  user_name = db.Column(db.String(64), index = True, unique = True)
  user_email = db.Column(db.String(120), index = True, unique = True)
  user_role = db.Column(db.SmallInteger, default = ROLE_USER)

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_userId(self):
    return unicode(self.user_id)
    
  def __repr__(self):
    return '<User %r>' % (self.user_name)