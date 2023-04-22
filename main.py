from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

db = SQLAlchemy(app)

class UrlInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True, nullable=False)
    short = db.Column(db.String(6), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now)

db.create_all()

# TODO: Home page
@app.route('/')
def index():
    return render_template('index.html')


# TODO: Urls page
@app.route('/urls')
def urls():
    return render_template('urls.html')
    # pass


# TODO: Redirect page
@app.route('/<short>')
def url_redirect(short):
    url = f"http://127.0.0.1:5000/{short}"
    return url

@app.route("/hi")
def hi():
    pass


if __name__ == '__main__':
    app.run(debug=True)
