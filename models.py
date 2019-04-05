from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:asd123@localhost:5432/sharks1')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Shark(db.Model):
    __tablename__ = 'sharks'
    name = db.Column(db.String(80), nullable = False, primary_key = True)
    url = db.Column(db.String(90), nullable = False)
    invested = db.Column(db.String(20))
    deals = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    picture = db.Column(db.String(1000), nullable = False)
    investments = db.Column(db.ARRAY(db.String(80)))
    investmentsURL = db.Column(db.ARRAY(db.String(80)))

class Investment(db.Model):
    __tablename__ = 'deal'
    name = db.Column(db.String(80), nullable = False)
    url = db.Column(db.String(90), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    episode = db.Column(db.String(80), nullable = False)
    founders = db.Column(db.ARRAY(db.String(40)), nullable = True)
    location = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    investment = db.Column(db.String(80))
    equity = db.Column(db.String(10))
    picture = db.Column(db.String(1000))
    sharks = db.Column(db.ARRAY(db.String(80)))
    sharksURL = db.Column(db.ARRAY(db.String(80)))

db.drop_all()
db.create_all()
