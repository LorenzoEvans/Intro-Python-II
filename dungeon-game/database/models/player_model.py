from ..app import database
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
