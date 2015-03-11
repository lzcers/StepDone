import os

CSRF_ENABLED = True
SECRET_KEY = '3.1415926p'
TASK_PER_PAGE = 10
# SQL config
basedir = os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:19931127@192.168.1.103:3306/GetDone'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')