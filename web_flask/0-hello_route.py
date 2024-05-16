#!/usr/bin/python3
""" simple script to begin with Flask """
from flask import Flask

app =  Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route decorator to specify the URL '/' for the function hello_hbnb. Returns a greeting message 'Hello HBNB!'.
    """
    return("Hello HBNB!")
app.run(host='0.0.0.0', port=5000)
