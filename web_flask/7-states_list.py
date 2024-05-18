#!/usr/bin/python3
from flask import Flask, url_for, render_template
from models import storage
from models.state import State


app =  Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def list_states():
    return render_template("7-states_list.html", states=storage.all(State))

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage
    """
    storage.close()

app.run(host='0.0.0.0', port=5000)
