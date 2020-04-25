from .room import Room
from .player import Player
from .item_set.armor import Shield
from .item_set.potions import Elixir
from .item_set.spell import Fire_Spell, Ice_Spell, Water_Spell, Earth_Spell, Air_Spell
from .item_set.weapons import BroadSword, LongSword

# Declare all the rooms

room = {
    'outside': Room('Entrance', 'Outside the Cave Entrance',
                    'North of you, the cave opening beckons'),

    'foyer': Room('Foyer', 'Dim light filters in from the south.',
                  'Dusty passages run north and east.',
                  [Shield, BroadSword]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Elixir, Fire_Spell]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Ice_Spell, Water_Spell]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [LongSword, Earth_Spell, Air_Spell]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
rogue = Player('Constantine', 100, 5, 10, 100, {}, room['outside'])


# input_data = input('')

# repl_parser()

def quit():
    print('You have exited The Crystalline Prophecy. Good-bye!')
    exit()
    # actions

    search = 'search'
    grab = 'grab'


def try_dir(dir, current_room):
    dir_choice = dir + '_to'
    if hasattr(current_room, dir_choice):
        return True
    else:
        return False


print('Welcome to The Crystalline Prophecy.')

while True:
    n = 'n'
    s = 's'
    e = 'e'
    w = 'w'
    q = 'q'
    r = 'r'
    # add wasd directional info
    item = ''
    input_data = input('> ').lower()
    if input_data == n:
        if try_dir(input_data, rogue.current_room):
            print('You went north.')
            rogue.current_room = rogue.current_room.n_to
            print(rogue.current_room.desc)
            print(rogue.__repr__())
            print('Current location: %s' % (rogue.current_room.name))
        else:
            print('There\'s nowhere for %s to go.' % (rogue.name))

    elif input_data == s:
        if try_dir(input_data, rogue.current_room):
            print('You went south.')
            rogue.current_room = rogue.current_room.s_to
            print('Current location: %s' % (rogue.current_room.name))
            print(rogue.current_room.desc)
            print(rogue.__repr__())
        else:
            print('There\'s nowhere for %s to go.' % (rogue.name))

    elif input_data == w:
        if try_dir(input_data, rogue.current_room):
            print('You went west.')
            rogue.current_room = rogue.current_room.w_to
            print('Current location: %s' % (rogue.current_room.name))
            print(rogue.current_room.desc)
            print(rogue.__repr__())
    elif input_data == e:
        if try_dir(input_data, rogue.current_room):
            print('You went east.')
            rogue.current_room = rogue.current_room.e_to
            print(rogue.current_room.desc)
            print(rogue.__repr__())
            print('Current location: %s' % (rogue.current_room.name))
        else:
            print('There\'s nowhere for %s to go.' % (rogue.name))

    if input_data == 'search':
        rogue.search(rogue.current_room)

    if input_data == 'grab':
        print('What item would you like to grab?')
        choice = input()
        while rogue.current_room.items is not None:
            for item in rogue.current.room_items:
                if item.item_name.lower() == choice.lower():
                    rogue.grab_item(rogue.current_room.items, item)
    if input_data == q:
        # Note, run a save all the things function here to keep progress
        # Push game state to object on start, diff that object and game state upon quit
        # over write changes
        quit()
