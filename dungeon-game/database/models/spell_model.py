from app import database
from sqlalchemy.orm import relationship 
from player_model import Player 

class Spell(database.Model):
  __tablename__ = 'spells'
  spell_id = database.Column('spell_id', database.Integer)
  spell_owner = relationship(Player, backref='spells')
  spell_name = database.Column('spell_name', database.String(256))
  spell_desc = database.Column('spell_desc', database.String)
  spell_type = database.Column('spell_type', database.String)
  spell_atk = database.Column('atk', database.Integer)
  magic_cost = database.Column('magic_cost', database.Integer)

  def __repr__(self):
    return '<Spell %r>' % self.spell_desc
