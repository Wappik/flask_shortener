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


# TODO: Redirect page
@app.route('/<short>')
def url_redirect(short):
    pass

@app.route("/hi")
def hi():
    pass


if __name__ == '__main__':
    app.run(debug=True)
