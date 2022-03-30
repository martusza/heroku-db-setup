import os
import psycopg2
import time
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DATABASE_URL = os.environ['DATABASE_URL']
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace("postgres", "postgresql")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)


db.create_all()

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        id_num = int(time.time())
        nickname = request.form.get("name", "Wojtek")
        email = request.form.get("email", "wojtek@bambi.pl")
        user = User(id=id_num, nickname=nickname, email=email)
        db.session.add(user)
        db.session.commit()
        return render_template("main.html")
    return render_template("main.html")