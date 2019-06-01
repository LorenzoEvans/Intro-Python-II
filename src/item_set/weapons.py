from items import Weapon

class BroadSword(Weapon):
 def __init__(self,
              name,
              desc,
              type,
              attack):
  self.name = name
  self.desc = desc
  self.type = type
  self.attack = attack

class LongSword(Weapon):
 def __init__(self,
              name,
              desc,
              type,
              attack):
  self.name = name
  self.desc = desc
  self.type = type
  self.attack = attack
