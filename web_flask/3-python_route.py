#!/usr/bin/python3
""" script that start flask web application """
from flask import Flask, url_for

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

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route decorator to specify the URL '/c/<text>' for the function c_text. Returns a greeting message 'C <text>'.
    """
    return("C {}".format(text.replace(" ", "_")))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Route decorator to specify the URL '/python/<text>' for the function python_text. Returns a greeting message 'Python <text>'.
    """
    #print(url_for('python_text', text=text.replace(" ", "_")))
    return("Python {}".format(text.replace(" ", "_")))

app.run(host='0.0.0.0', port=5000, debug=True)
