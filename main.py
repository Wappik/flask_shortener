from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from datetime import datetime

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import string
import random
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


class FromURL(FlaskForm):
    original_url = StringField('Url',
                               validators=[DataRequired(message="fill URL!")])
    submit = SubmitField("get short url.")


def get_short_url():
    active = True
    while active is True:
        short = "".join(random.choices(string.ascii_letters + string.ascii_letters, k=6 ))

        if UrlInfo.query.filter(UrlInfo.short == short).first():
            pass
        else:
            return short

db = SQLAlchemy(app)

class UrlInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True, nullable=False)
    short = db.Column(db.String(6), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now)

db.create_all()
db = SQLAlchemy(app)

class UrlInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True, nullable=False)
    short = db.Column(db.String(6), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now)

db.create_all()

# TODO: Home page
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# TODO: Urls page
@app.route('/urls')
def urls():
    return render_template('urls.html')
    # pass


@app.route('/<string:short>', methods=['GET'])
def url_redirect(short):
    url = UrlInfo.query.filter(UrlInfo.short == short).first()
    if url:
        url.visits += 1
        db.session.add(url)
        db.session.commit()
        return url_redirect(url.original_url)


@app.route("/hi")
def hi():
    pass


if __name__ == '__main__':
    app.run(debug=True)
