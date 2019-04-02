from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

sql = os.environ.get('SQL_URI')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sql
db = SQLAlchemy(app)

from pkg import routes