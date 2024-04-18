#!/usr/bin/python3

from models.state import State
from models.city import City
from models import storage


new_state = State(name="California")
storage.new(new_state)

# new_cities = []
# new_city1 = City(name="San Francisco")
# new_cities.append(new_city1)
# new_city2 = City(name="Los Angeles")
# new_cities.append(new_city2)

storage.save()


