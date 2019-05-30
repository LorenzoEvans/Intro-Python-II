# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
 def __init__(self, 
              name, 
              health, 
              attack, 
              defense, 
              magic, 
              pouch,
              current_room):
  self.name = name
  self.health = health
  self.attack = attack
  self.defense = defense
  self.magic = magic
  self.current_room = current_room