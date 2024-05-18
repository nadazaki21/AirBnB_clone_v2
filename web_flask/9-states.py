#!/usr/bin/python3
from flask import Flask, url_for, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv


app =  Flask(__name__)


app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def  list_states(id=None):
    if id is None:
        return render_template("9-states.html", states=storage.all(State), id=None)
    else:
        all=storage.all(State)
        #print(id)
        for key in all.keys():
            #print(key)
            if id == key:
                if getenv("HBNB_TYPE_STORAGE") == "db":
                    return render_template("9-states.html", states=storage.all(State), cities=storage.all(City), id = id)
                else:
                    return render_template("9-states.html", states=storage.all(State), cities=State.cities,  id = id)
        
        return render_template("9-states.html", id="notfound")
    
@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage
    """
    storage.close()

app.run(host='0.0.0.0', port=5000)
