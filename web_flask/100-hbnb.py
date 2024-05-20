#!/usr/bin/python3
from flask import Flask, url_for, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import getenv


app =  Flask(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/hbnb', strict_slashes=False)
def search_filetrs():
    if getenv ("HBNB_TYPE_STORAGE") == "db":
        return render_template("100-hbnb.html", states=storage.all(State), amenities=storage.all(Amenity), places=storage.all(Place), cities=storage.all(City))
    else:
        return render_template("100-hbnb.html", states=storage.all(State), amenities=storage.all(Amenity), places=storage.all(Place), cities=State.cities)
def teardown_db(exception):
    """
    Closes the storage
    """
    storage.close()

app.run(host='0.0.0.0', port=5000, debug=True)
