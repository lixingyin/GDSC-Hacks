from flask import Flask
from flask import redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = request.form['subject']
        text1 = request.form['text']
        text2 = request.form['time']        

        allWords = text1.split()
        print("Words:", allWords)  
        return render_template('result.html', allWords=allWords, text=text, text2=text2)
    return render_template('result.html', allWords=[], text=text, text2=text2)

if __name__ == '__main__':
    app.run(debug=True)
    
# flask --app main run