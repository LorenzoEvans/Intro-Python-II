# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
 def __init__(self, name, location, cardinal_dir, items, monsters):
  self.name = name
  self.location = location
  self.cardinal_dir = cardinal_dir
  items = {}
  monsters = {}