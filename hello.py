from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'

bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


@app.route("/")
def hello():
    fruits = ['apple', 'banana', 'orange']
    return render_template('index.html', fruits=fruits)


@app.route("/user/<name>")
def user(name):

    return render_template('user.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
