from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:asd123@localhost:5432/sharks')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

class Shark(db.Model):
    __tablename__ = 'sharks'
    name = db.Column(db.String(80), nullable = False, primary_key = True)
    invested = db.Column(db.String(20))
    deals = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    picture = db.Column(db.String(80), nullable = False)
    investments = db.Column(db.ARRAY(db.Integer))

class Investment(db.Model):
    __tablename__ = 'deal'
    name = db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    episode = db.Column(db.String(80), nullable = False)
    founders = db.Column(db.ARRAY(db.String(40)), nullable = True)
    location = db.Column(db.String(80))
    description = db.Column(db.String(140))
    investment = db.Column(db.String(80))
    equity = db.Column(db.String(10))
    picture = db.Column(db.String(140))
    sharks = db.Column(db.ARRAY(db.String(80)))


db.create_all()
