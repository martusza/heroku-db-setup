import os
import psycopg2
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DATABASE_URL = os.environ['DATABASE_URL']
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)



@app.route("/")
def main():
    return "Hello World"