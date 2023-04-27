from flask import Flask, render_template, url_for

app = Flask(__name__)


# TODO: Home page
@app.route('/')
def index():
    return render_template('index.html')


# TODO: Urls page
@app.route('/urls')
def urls():
    return render_template('urls.html')
    # pass


@app.route('/<string:short>', methods=['GET'])
def url_redirect(short):
    url = URLmodel.query.filter(URLmodel.short == short).first()
    if url:
        url.visits += 1
        db.session.add(url)
        db.session.commit()
        return url_redirect(url.original_url)


if __name__ == '__main__':
    app.run(debug=True)
