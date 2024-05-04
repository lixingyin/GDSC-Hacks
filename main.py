from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hello, World'

# flask --app main run