class Item:
 def __init__(self, 
              name, 
              desc, 
              type = None, 
              attack = None, 
              defense = None):
  self.name = name
  self.desc = desc
  self.type = type if type is not None else type
  self.attack = attack if attack is not None else attack
  self.defense = defense if defense is not None else defense

class Potion(Item):
 def __init__(self,
              name,
              desc,
              type):
  self.name = name
  self.desc = desc
  self.type = type

class Weapon(Item):
 def __init__(self,
              name,
              desc,
              type,
              attack):
  self.name = name
  self.desc = desc
  self.type = type
  self.attack = attack
 
class Armor(Item):
 def __init__(self,
              name,
              desc,
              type,
              defense):
  self.name = name
  self.desc = desc
  self.type = type
  self.defense = defense

# class Spell
