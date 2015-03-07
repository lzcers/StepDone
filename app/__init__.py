import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir

app = Flask(__name__)

# load config
app.config.from_object('config')

# connect db
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

# load views
from app import views, models