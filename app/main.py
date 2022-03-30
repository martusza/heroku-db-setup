import os
import psycopg2
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

DATABASE_URL = os.environ['DATABASE_URL']
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')