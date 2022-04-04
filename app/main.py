import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace("postgres", "postgresql")
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)


db.create_all()


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        nickname = request.form.get("name")
        email = request.form.get("email")
        user = User(nickname=nickname, email=email)
        db.session.add(user)
        db.session.commit()
        table = User.query.all()
        return render_template("main.html", table=table)
    table = User.query.all()
    return render_template("main.html", table=table)