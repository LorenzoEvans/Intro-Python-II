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
  self.type = item_type if item_type is not None else item_type
  self.attack = attack if attack is not None else attack
  self.defense = defense if defense is not None else defense

class Potion(Item):
 def __init__(self,
              name,
              desc,
              type,
              potency = None,
              quantity = 0):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = type
  self.potency = 5 if potency is not None else potency

class SmallPotion(Potion):
 def __init__(self,
              name,
              desc,
              type,
              quantity):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = type

class MediumPotion(Potion):
 def __init__(self,
              name,
              desc,
              type,
              quantity):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = type

class LargePotion(Potion):
 def __init__(self,
              name,
              desc,
              type,
              quantity):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = type


class Weapon(Item):
 def __init__(self,
              name,
              desc,
              type,
              attack,
              quantity):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = type
  self.attack = attack

class BroadSword(Weapon):
 def __init__(self,
              name,
              desc,
              type,
              attack,
              quantity):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = type
  self.attack = attack

class LongSword(Weapon):
 def __init__(self,
              name,
              desc,
              type,
              attack,
              quantity):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = type
  self.attack = attack


class Armor(Item):
 def __init__(self,
              name,
              desc,
              type,
              defense,
              quantity):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = type
  self.defense = defense

class Spell(Item):
 def __init__(self,
              name,
              desc,
              spell_type,
              attack,
              cost,
              quantity):
  super.__init__(quantity)
  self.name = name
  self.desc = desc
  self.type = spell_type
  self.attack = attack
  self.cost = cost

item_types = ['spell', 'armor', 'weapon', 'potion']