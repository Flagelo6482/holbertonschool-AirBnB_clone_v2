#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def strict_slashes=False():
    """Function to say hello"""
    return "Hello HBNB!"
