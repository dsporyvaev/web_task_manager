from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///taskmaster.db'
db = SQLAlchemy(app)

from taskmanager import routes








