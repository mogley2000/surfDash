from flask import Flask, render_template
from scraper import runScraper

app = Flask(__name__)   # app object from Flask class. Argument is __name__
@app.route("/")
def home():
    flask_runScraper = runScraper()
    return render_template('home.html', runScraper=flask_runScraper)

@app.route('/salvador')
def salvador():
    return('Hello Salvador')

@app.route('/about')
def about():
    name = "Monkey Rabbit testing Jinja"
    return (name)

@app.route('/manly')
def manly():
    flask_runScraper = runScraper()
    return render_template('manly.html', runScraper=flask_runScraper)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
