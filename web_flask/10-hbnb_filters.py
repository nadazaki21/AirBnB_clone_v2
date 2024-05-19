#!/usr/bin/python3
from flask import Flask, url_for, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import getenv


app =  Flask(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/hbnb_filters', strict_slashes=False)
def search_filetrs():
    if getenv("HBNB_TYPE_STORAGE") == "db":
        return render_template("10-hbnb_filters.html", amenities=storage.all(Amenity), cities=storage.all(City), states=storage.all(State))
    else:
        return render_template("10-hbnb_filters.html", amenities=storage.all(Amenity), cities=State.cities, states=storage.all(State))
def teardown_db(exception):
    """
    Closes the storage
    """
    storage.close()

app.run(host='0.0.0.0', port=5000)
