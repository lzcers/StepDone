from app import db
from app.models import User
test_user = User('test', 'test')
db.session.add(test_user)
db.session.commit()
db.create_all()
