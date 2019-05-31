from room import Room
from player import Player

# Declare all the rooms
 
room = {
    'outside':  Room("Outside the Cave Entrance",
                     "North of you, the cave opening beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
 
 input_data = input('> ').lower()
 if input_data == n:
  if try_dir(input_data, rogue.current_room):
   print('You went north.')
   rogue.current_room = rogue.current_room.n_to
   print(rogue.current_room.desc)
   print('Current location: %s' % (rogue.current_room.name))
  else:
   print('There\'s nowhere for %s to go.' % (rogue.name))
 elif input_data == s:
  if try_dir(input_data, rogue.current_room):
   print('You went south.')
   rogue.current_room = rogue.current_room.s_to
   print('Current location: %s' % (rogue.current_room.name))
   print(rogue.current_room.desc)
  else:
   print('There\'s nowhere for %s to go.' % (rogue.name))
 elif input_data == w:
  if try_dir(input_data, rogue.current_room):
   print('You went west.')
   rogue.current_room = rogue.current_room.w_to
   print('Current location: %s' % (rogue.current_room.name))
   print(rogue.current_room.desc)
 elif input_data == e:
  if try_dir(input_data, rogue.current_room):
   print('You went east.')
   rogue.current_room = rogue.current_room.e_to
   print(rogue.current_room.desc)
   print('Current location: %s' % (rogue.current_room.name))
  else:
   print('There\'s nowhere for %s to go.' % (rogue.name))
 elif input_data == q:
  quit()


# Write a loop that:
#
# * Prints the current room name
    # print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    # print(player.current_room.desc)
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# for data in room:
#  q = 'q'
#  print(data)
#  dir_choice = input('')
#  if dir_choice == q:
  # print('Goodbye') # already made this message elsewhere, 
  # quit() (write quit function at some point)

print(rogue)