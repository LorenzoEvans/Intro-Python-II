potion = 'potion'
weapon = 'weapon'
spell = 'spell'
armor = 'armor'
class Item:
 def __init__(self, 
              name, 
              desc, 
              quantity,
              item_type = None, 
              attack = None, 
              defense = None):
  self.name = name
  self.desc = desc
  self.quantity = quantity
  self.type = item_type if item_type is not None else item_type
  self.attack = attack if attack is not None else attack
  self.defense = defense if defense is not None else defense

class Potion(Item):
 def __init__(self, name, desc, item_type, quantity, potency=None):
   super().__init__(name, desc, quantity, item_type)
   self.name = name
   self.desc = desc
   self.type = item_type if item_type is not None else item_type
   self.potency = 100 if potency is not None else potency
   # Potency doesn't define health points returned,
   # but rather the percentage of health returned. booyah

class SmallPotion(Potion):
 def __init__(self, name, desc, item_type, quantity):
  super().__init__(name, desc, item_type, quantity)
  self.name = name
  self.desc = desc
  self.type = item_type

class MediumPotion(Potion):
 def __init__(self, name, desc, item_type, quantity):
  super().__init__(name, desc, item_type, quantity)
  self.name = name
  self.desc = desc
  self.type = item_type

class LargePotion(Potion):
 def __init__(self, name, desc, item_type, quantity):
  super().__init__(name, desc, item_type, quantity)
  self.name = name
  self.desc = desc
  self.type = item_type


class Weapon(Item):
 def __init__(self, name, desc, item_type, attack, quantity):
  super().__init__(name, desc, quantity, item_type, attack)
  self.name = name
  self.desc = desc
  self.type = item_type
  self.attack = attack

class BroadSword(Weapon):
 def __init__(self, name, desc, item_type, attack, quantity):
  super().__init__(name, desc, item_type, attack, quantity)
  self.name = name
  self.desc = desc
  self.type = item_type
  self.attack = attack

class LongSword(Weapon):
 def __init__(self, name, desc, item_type, attack, quantity):
  super().__init__(name, desc, item_type, attack, quantity)
  self.name = name
  self.desc = desc
  self.type = item_type
  self.attack = attack


class Armor(Item):
 def __init__(self, name, desc, item_type, defense, quantity):
  super().__init__(name, desc, quantity, item_type, defense)
  self.name = name
  self.desc = desc
  self.type = item_type
  self.defense = defense

class Spell(Item):
 def __init__(self, name, desc, item_type, attack, cost, quantity):
  super().__init__(name, desc, quantity, item_type, attack)
  self.name = name
  self.desc = desc
  self.type = item_type
  self.attack = attack
  self.cost = cost

item_types = [spell, armor, potion, weapon]