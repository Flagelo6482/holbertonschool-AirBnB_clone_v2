#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def rout():
    """Route '/'"""
    return "Hello HBNB!"


@app.route('/', strict_slashes=False)
def hbnb():
    """Route '/hbnb'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    """Adding an argument to the definition"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Function that receives an argument"""
    if text == '':
        text = 'is cool'
    else:
        text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
