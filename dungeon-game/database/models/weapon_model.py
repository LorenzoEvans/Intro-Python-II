from ..app import database 
from ..sqlalchemy.orm import relationship 
from player_model import Player 
class Weapon(database.Model):
  __tablename__ = 'weapons'
  weapon_id = database.Column('weapon_id', database.Integer)
  owner = relationship(Player, backref='weapons')