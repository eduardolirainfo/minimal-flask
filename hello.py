from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/user/<name>")
def user(name):

    return render_template('user.html', name=name)
    # return "<h1>Hello, %s!</h1>" % name
    # or
    # f"<h1>Hello, {name}!</h1>"
    # or
    # return "<h1>Hello, {}!</h1>".format(name)


if __name__ == "__main__":
    app.run(debug=True)
