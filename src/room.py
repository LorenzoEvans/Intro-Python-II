# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
 def __init__(self, 
              name, 
              desc, 
              items = [], 
              monsters = None,
              current_player = None,
              n_to = None,
              s_to = None,
              w_to = None,
              e_to = None):
  self.name = name
  self.desc = desc
  self.current_player = current_player
  self.items = [] if items is None else items
  monsters = {} if items is None else items
  self.current_player = current_player if current_player is not None else current_player
  self.n_to = n_to if n_to is not None else n_to
  self.s_to = s_to if s_to is not None else s_to
  self.w_to = w_to if w_to is not None else w_to
  self.e_to = e_to if w_to is not None else w_to
#  def __repr__(self):
#   return f"{self.name} {self.desc}, {self.current_player}."