from flask import Flask
from flask import redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = request.form['text']
        words = text.split()
        print("Words:", words)  
        return render_template('result.html', words=words)
    return render_template('result.html', words=[])


# flask --app main run