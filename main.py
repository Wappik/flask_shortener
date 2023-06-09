from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import string
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class UrlInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True, nullable=False)
    short = db.Column(db.String(6), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now)


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


# TODO: Home page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = FromURL()
    if form.validate_on_submit():
        # setter for url
        url = UrlInfo()
        url.short = get_short_url()
        url.original_url = form.original_url.data
        # commit
        db.session.add(url)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template('index.html', form=form)


# TODO: Urls page
@app.route('/urls')
def urls():
    urls = UrlInfo.query.all()
    return render_template('urls.html', urls=urls[::-1])


@app.route('/<string:short>', methods=['GET'])
def url_redirect(short):
    url = UrlInfo.query.filter(UrlInfo.short == short).first()
    if url:
        url.visits += 1
        db.session.add(url)
        db.session.commit()
        return redirect(url.original_url)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
