from ast import literal_eval
from database.models.player_model import Player
from database.models.spell_model import Spell
from database.base import Base 
import logging 
import sys

log = logging.getLogger(__name__)
logging.basicConfig(
  stream=sys.stdout,
  level=logging.INFO,
  format='%(asctime)s - %(name)s- %(levelname)s - %(message)s')
if __name__ == '__main__':
  log.info('Create database {}'.format(Base.db_name))
  Base.Base.metadata.create_all(Base.engine)
  log.info('Insert Player data into database.')
  with open('database/data/Players.json', 'r') as file:
    data = literal_eval(file.read())
    for record in data:
      player = Player(**record)
      Base.db_session.add(player)
    Base.db_session.commit()
  log.info('Insert Spell data in database.')
  with open ('database/data/Spells.json') as file:
    data = literal_eval(file.read())
    for record in data:
      spell = Spell(**record)
      Base.db_session.add(planet)
    Base.db_session.commit
  

