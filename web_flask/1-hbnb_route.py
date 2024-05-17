#!/usr/bin/python3
""" script that start flask web application """
from flask import Flask

app =  Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route decorator to specify the URL '/' for the function hello_hbnb. Returns a greeting message 'Hello HBNB!'.
    """
    return("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route decorator to specify the URL '/hbnb' for the function hbnb. Returns a greeting message 'HBNB'.
    """
    return("HBNB")

app.run(host='0.0.0.0', port=5000)
