#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def strict_slashes=False():
    return "Hello HBNB!"
