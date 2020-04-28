from ..app import database

class Player(database.Model):
  __tablename__ = "players"
  uuid = database.Column('uuid', database.Integer, primary_key=True)
  player_name = database.Column('player_name', database.String(256), index=True, unique=True)
  health = database.Column('health', database.Integer)
  level = database.Column('level', database.Integer)
  exp = database.Column('exp', database.Integer)
  attack = database.Column('attack', database.Integer)
  defense = database.Column('defense', database.Integer)
  magic = database.Column('magic', database.Integer)
  # Relationships
  # spells_list = relationship(Spell, backref='players')
  # weapons_list = relationship(Spell, backref='players')
  # potions_list = relationship(Spell, backref='players')
  # armor_list = relationship(Spell, backref='players')

  equipped_armor = database.Column('equipped_armor', database.String)
  equipped_weapon = database.Column('equipped_weapon', database.String)
  def __repr__(self):
    return '<Player %r>' % self.player_name
