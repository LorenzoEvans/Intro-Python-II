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
              type,
              potency = None):
  self.name = name
  self.desc = desc
  self.type = type
  self.potency = 5 if potency is not None else potency

class SmallPotion(Potion):
 def __init__(self,
              name,
              desc,
              type):
  self.name = name
  self.desc = desc
  self.type = type

class MediumPotion(Potion):
 def __init__(self,
              name,
              desc,
              type):
  self.name = name
  self.desc = desc
  self.type = type

class LargePotion(Potion):
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

class Spell(Item):
 def __init__(self,
              name,
              desc,
              type,
              attack):
  self.name = name
  self.desc = desc
  self.type = type
  self.attack = attack
