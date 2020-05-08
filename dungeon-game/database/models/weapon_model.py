from ..app import database 
from ..sqlalchemy.orm import relationship 
from player_model import Player 
class Weapon(database.Model):
  __tablename__ = 'weapons'
  weapon_id = database.Column('weapon_id', database.Integer)
  weapon_name = database.Column('weapon_name', database.String(256))
  weapon_desc = database.Column('weapon_desc', database.String(256))
  weapon_atk = database.Column('weapon_atk', database.Integer)
  weapon_owner = relationship(Player, backref='weapons')

  def __repr__(self):
    return '<Weapon %r>' % self.weapon_desc