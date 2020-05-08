from ..app import database 
from ..sqlalchemy.orm import relationship 
from player_model import Player 

class Potion(database.Model):
  __tablename__ = 'potions'
  potion_size = database.Column('potion_size', database.String)
  potion_desc = database.Column('potion_desc', database.String)
  potion_potency = database.Column('potency', database.Integer)
  owner = relationship(Player, backref='potions')

  def __repr__(self):
    return '<Potion %r>' % self.potion_desc