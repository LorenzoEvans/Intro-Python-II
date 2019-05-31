# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
 def __init__(self, 
              name, 
              health, 
              attack, 
              defense, 
              magic, 
              pouch = None,
              current_room = None):
  self.name = name
  self.health = health
  self.attack = attack
  self.defense = defense
  self.magic = magic
  pouch = {} if pouch is None else pouch
  self.current_room = current_room if current_room is not None else current_room
 def __repr__(self):
  return f"You have {self.health} health, {self.attack} attack, {self.defense} defense, {self.magic} magic, and are {self.current_room}."
 def grab_item(self):
  print('Grabbed item')