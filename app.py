from flask import Flask, render_template
from scraper import elemDate

app = Flask(__name__)   # app object from Flask class. Argument is __name__
@app.route("/")
def home():
    return render_template('home.html', elemDate=elemDate)

@app.route('/salvador')
def salvador():
    return('Hello Salvador')

@app.route('/about')
def about():
    name = "Monkey Rabbit testing Jinja"
    return render_template('about.html', name=name)

@app.route('/manly')
def manly():
    return render_template('manly.html')

