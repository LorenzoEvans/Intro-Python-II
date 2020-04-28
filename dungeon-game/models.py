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






class Armor(database.Model):
  __tablename__ = 'armors'
  player_id = database.Column('armor_uuid', database.Integer, database.ForeignKey('player.uuid'))


