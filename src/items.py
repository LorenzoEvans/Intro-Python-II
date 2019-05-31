class Item:
 def __init__(self, 
              name, 
              desc, 
              type = None, 
              attack = None, 
              defense = None):
  self.name = name
  self.desc = desc
  self.type = type
  self.attack = attack
  self.defense = defense

class Potion(Item):
 def __init__(self)