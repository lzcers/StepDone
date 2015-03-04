import os

CSRF_ENABLED = True
SECRET_KEY = '3.1415926p'

# SQL config
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:19931127@192.168.1.103:3306/GetDone'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')