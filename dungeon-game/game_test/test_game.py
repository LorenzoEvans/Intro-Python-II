
import unittest
from game.player import Player 
from game.room import Room
from game.item_set.items import Item, MediumPotion, LargePotion, Weapon, BroadSword, LongSword, Armor
from game.item_set.potions import Elixir
from game.item_set.armor import Shield
from game.item_set.spell import Fire_Spell, Ice_Spell, Water_Spell, Earth_Spell, Air_Spell

class TestElixir(unittest.TestCase):
  def test_elixir(self):
    elixir = Elixir()
    player = Player()
    player.use_postion(elixir)


if __name__ == '__main__':
    unittest.main()