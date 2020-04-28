from ast import literal_eval
from ..database.models.player_model import Player
from ..database.models.spell_model import Spell
from ..database.base import base 
import logging 
import sys

log = logging.getLogger(__name__)
logging.basicConfig(
  stream=sys.stdout,
  level=logging.INFO,
  format='%(asctime)s - %(name)s- %(levelname)s - %(message)s')


if __name__ == '__main__':
  
  log.info('Create database {}'.format(base.db_name))
  
  base.Base.metadata.create_all(base.engine)
  
  log.info('Insert Player data into database.')
  
  with open('database/data/player.json', 'r') as file:

    data = literal_eval(file.read())

    for record in data:
      
      player = Player(**record)
      base.db_session.add(player)
    base.db_session.commit()
  

