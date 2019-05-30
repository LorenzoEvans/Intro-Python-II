# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
 def __init__(self, 
              name, 
              desc, 
              cardinal_dir,
              items, 
              monsters,
              current_player,
              n_to,
              s_to,
              w_to,
              e_to):
  self.name = name
  self.desc = desc
  self.cardinal_dir = '' if cardinal_dir is None else cardinal_dir
  items = {} if items is None else items
  monsters = {} if items is None else items
  self.current_player = current_player
  self.n_to = n_to
  self.s_to = s_to
  self.w_to = w_to
  self.e_to = e_to