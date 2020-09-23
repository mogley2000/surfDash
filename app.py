from flask import Flask, render_template
import scraper
from tabulate import tabulate 

app = Flask(__name__)   # app object from Flask class. Argument is __name__
@app.route("/")
def home():
    tabulated = scraper.tabulated
    return render_template('home.html', tabulated=tabulated)

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

