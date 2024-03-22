#!/usr/bin/python3
""" script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """HELLO HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ HBNB!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """C is FUN but we are DONE!!"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Python is cool , Dont be fool
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """is it a number?
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """number_template -> 5-number.html
    """
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
