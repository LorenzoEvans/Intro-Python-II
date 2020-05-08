from ..app import database 
from ..sqlalchemy.orm import relationship 
from player_model import Player 

class Armor(database.Model):
  __tablename__ = 'armors'
  player_id = database.Column('armor_id', database.Integer, database.ForeignKey('player.id'))
  armor_name = database.Column('armor_name', database.String(256))
  armor_desc = database.Column('armor_desc', database.String(256))
  armor_defense = database.Column('defense', database.Integer)
  owner = relationship(Player, backref='armors')

  def __repr__(self):
    return '<Armor %r>' % self.armor_desc