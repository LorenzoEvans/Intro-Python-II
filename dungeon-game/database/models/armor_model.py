from ..app import database 
from ..sqlalchemy.orm import relationship 
from player_model import Player 

class Armor(database.Model):
  __tablename__ = 'armors'
  player_id = database.Column('armor_id', database.Integer, database.ForeignKey('player.id'))