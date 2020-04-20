# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
 def __init__(self, 
              name, 
              health, 
              attack, 
              defense, 
              magic, 
              inventory = None,
              current_room = None):
  self.name = name
  self.health = health
  self.attack = attack
  self.defense = defense
  self.magic = magic
  self.spells = []
  self.potions = []
  self.armors = []
  self.equipped_armor = None
  self.equipped_weapon = None 
  self.equipped = [self.equipped_armor, self.equipped_weapon]
  self.weapons = []
  self.inventory = {spells: self.spells, 
                    potions: self.potions,
                    armors: self.armor,
                    weapons: self.weapons,
                    equipped: [self.equipped_armor, self.equipped_weapon]} if inventory is None else inventory
  self.current_room = current_room if current_room is not None else current_room

 def search(self, current_room):
  if len(current_room.items) > 0:
   for item in current_room.items:
    print(item.name)
  elif len(current_room.items) == 0:
   print("This room is empty.")
 
 def equip_item(self, item):
   if item.item_type is 'weapon' and item in self.inventory.weapons:
    self.equipped_weapon = item
   elif item.item_type is 'armor' and item in self.inventory.armors:
     self.equipped_armor = item
   else:
     return f"You do not have this item. You can only equip items if you have them. Try searching for it!"

 def grab_item(self, current_room, item_name):
   if item_name in current_room.items:
     self.inventory.insert(0, item_name)
     print(f"{self.name} grabbed the {item_name}.")

 def drop_item(self):
  print('Dropped item.')

 def __repr__(self):
  return f"You have {self.health} health, {self.attack} attack, {self.defense} defense, {self.magic} magic, and are in the {self.current_room}."