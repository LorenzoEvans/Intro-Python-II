# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
 def __init__(self,
              name,
              health,
              attack,
              defense,
              magic,
              inventory=None,
              current_room=None):
  self.name = name
  self.level = 0
  self.exp = 0
  self.health = health
  self.attack = attack
  self.defense = defense
  self.magic = magic
  self.spells = []
  self.current_room_items = []
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


# def cast(spell, target):
  # while self.magic >= spell.cost:
    # spell.use(target) # Note, if it's a status changing spell the target will be self..hmm

def search(self, current_room):
  if len(current_room.items) > 0:
    for item in current_room.items:
      self.current_room_items.insert(0, {item.item_name: item})
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
def drop_item(self, item):
  for section in self.inventory:
    if item in section:
      item_idx = section[section.index(item)]
      del section[item_idx]
  print('Dropped item.')

def check_inventory(self, inventory, item_name):
  for item in inventory:
    if item.item_name is item_name:
      return True 
    else:
      return False

def grab_item(self, current_room, item):
  if item.item_type is 'spell':
    if check_inventory(self.inventory, item.item_name):
      for spell in self.spells:
        if spell['spell_name'] is item.item_name:
          self.spells.index(spell).quantity += 1
          item_idx = current_room.items.index(item)
          del current_room.items[item_idx]
    else:
      self.spells.insert(0, {'spell_name': item.item_name, 'item': item, 'quantity': item.quantity})
      item_idx = current_room.items.index(item)
      current_room.items[item_idx] = None
      del current_room.items[item_idx]
  elif item.item_type is 'weapon':
    if check_inventory(self.inventory, item.item_name):
      for weapon in self.weapons:
        if weapon['weapon_name'] is item.item_name:
          self.weapons.index(weapon).quantity += 1
          item_idx = current_room.items.index(item)
          del current_room.items[item_idx]
    else:
      self.spells.insert(0, {'weapon_name': item.item_name, 'item': item, 'quantity': item.quantity})
      item_idx = current_room.items.index(item)
      current_room.items[item_idx] = None
      del current_room.items[item_idx]
  elif item.item_type is 'armor': 
    if check_inventory(self.inventory, item.item_name):
      for armor in self.armors:
        if armor['armor_name'] is item.item_name:
          self.armors.index(armor).quantity += 1
          item_idx = current_room.items[current_room.items.index(item)]
          del current_room.items[item_idx]
    else:
      self.spells.insert(0, {'armor_name': item.item_name, 'item': item, 'quantity': item.quantity})
      item_idx = current_room.items.index(item)
      current_room.items[item_idx] = None
      del current_room.items[item_idx]  
  elif item.item_type is 'potion':
    if check_inventory(self.inventory, item.item_name):
      for potion in self.potions:
        if potion.potion_name is item.item_name:
          self.potions.index(potion).quantity += 1
          item_idx = current_room.items.index(item)
          del current_room.items[item_idx]
    self.spells.insert(0, {'potion_name': item.item_name, 'item': item, 'quantity': item.quantity})
    item_idx = current_room.items.index(item)
    current_room.items[item_idx] = None
    del current_room.items[item_idx]
  print(f"{self.name} grabbed the {item.item_name} and added it to their inventory!")
def __repr__(self):
  return f"You have {self.health} health, {self.attack} attack, {self.defense} defense, {self.magic} magic, and are in the {self.current_room}."
