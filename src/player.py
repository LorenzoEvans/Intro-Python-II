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
 def search(self, current_room):
  if len(current_room.items) > 0:
   for item in current_room.items:
    print(item.name)
  elif len(current_room.items) == 0:
   print("This room is empty.")
 def grab_item(self, current_room):
  print('Grabbed item')
 def drop_item(self):
  print('Dropped item.')