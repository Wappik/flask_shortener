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
    url = f"http://127.0.0.1:5000/{short}"
    return url


if __name__ == '__main__':
    app.run(debug=True)
