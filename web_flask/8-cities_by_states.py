#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv

app =  Flask(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/cities_by_states", strict_slashes=False)
def list_cities_of_state ():
    if getenv("HBNB_TYPE_STORAGE") == "db":
        return render_template("8-cities_by_states.html", cities=storage.all(City), states=storage.all(State))
    else:
        return render_template("8-cities_by_states.html", cities=State.cities, states=storage.all(State))
    
@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage
    """
    storage.close()

app.run(host='0.0.0.0', port=5000)
