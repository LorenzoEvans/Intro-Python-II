from .app import database
from sqlalchemy.orm import relationship
# What is the relationship between players and items?
# A player can have many items obviously, but can an item, be held by many players? ?_?
# This depends on how we program the ownership of items.
# We don't want items to be held by more than one character.
# What difficulties does this pose?
  # * Generating unique ids for identical items.
    # * We may backtrack here because, how will we distinguish two
    # identical items to generate unique ids for them without the unique id?
    # We have to make id generation a part of the class instantiation,
    # which requires something to exist outside of the classes, but
    # capable of altering their state?
    # Are we over thinking?
    # We can distinguish between the object in the database, and say,
    # an instantiation of that object, via the difference in logic that handles,
    # retrieval from db, vs in game interaction.
class Spell(database.Model):
  __tablename__ = 'spells'
  spell_id = database.Column('spell', database.Integer, database.ForeignKey('player.uuid'))
  # spell_element/type
  # spell_damage
  # magic_cost
class Player(database.Model):
  __tablename__ = "players"
  uuid = database.Column('uuid', database.Integer, primary_key=True)
  player_name = database.Column('player_name', database.String(256), index=True, unique=True)
  health = database.Column('health', database.Integer)
  # items = database.relationship('')
  level = database.Column('level', database.Integer)
  exp = database.Column('exp', database.Integer)
  attack = database.Column('attack', database.Integer)
  defense = database.Column('defense', database.Integer)
  magic = database.Column('magic', database.Integer)
  spells_list = relationship(Spell, backref='players')
  weapons_list = relationship(Spell, backref='players')
  potions_list = relationship(Spell, backref='players')
  armor_list = relationship(Spell, backref='players')
  equipped_armor = database.Column('equipped_armor', database.String)
  equipped_weapon = database.Column('equipped_weapon', database.String)

  class Spell(database.Model):
    __tablename__ = 'spells'
    spell_id = database.Column('player_uuid', database.Integer, database.ForeignKey('player.uuid'))

  class Weapon(database.Model):
    __tablename__ = 'weapons'
    player_id = database.Column('player_uuid', database.Integer, database.ForeignKey('player.uuid'))

  class Potion(database.Model):
    __tablename__ = 'potions'
    potion_size = database.Column('potion_size', database.String)
    potion_desc = database.Column('potion_desc', database.String)
    player_id = database.Column('player_uuid', database.Integer, database.ForeignKey('player.uuid'))

  class Armor(database.Model):
    __tablename__ = 'armors'
    player_id = database.Column('player_uuid', database.Integer, database.ForeignKey('player.uuid'))

