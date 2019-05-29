from room import Room
from player import Player
from art import art

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
inputName = input('\x1b[1;33;40m' + "Please player's name: " + '\x1b[0m')
player = Player(inputName, room['outside'])
print('\x1b[0;36;40m' + "\n\n****************************************************" + '\x1b[0m' + "\n")
print('\x1b[0;36;40m' + f"Welcome {player.name}" + '\x1b[0m' + "\n")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


cmds = [
    "n", "s", "e", "w", 
    "N", "S", "E", "W",
    "North", "South", "East", "West",
    "north", "south", "east", "west"]

def direction(player, cmd):
    if cmd == "n" or cmd == "N" or cmd == "North" or cmd == "north":
        if player.current_room.n_to:
            dir = "Go North!"
            player.current_room = player.current_room.n_to
        else:
            return print('\x1b[0;33;40m' +"I'm sorry you can't go North." + '\x1b[0m')
    elif cmd == "s" or cmd == "S" or cmd == "South" or cmd == "south":
        if player.current_room.s_to:
            dir = "Go South!"
            player.current_room = player.current_room.s_to
        else:
            return print('\x1b[0;33;40m' + "I'm sorry you can't go South." + '\x1b[0m')
    elif cmd == "e" or cmd == "E" or cmd == "East" or cmd == "east":
        if player.current_room.e_to:
            dir = "Go East!"
            player.current_room = player.current_room.e_to
        else:
            return print('\x1b[0;33;40m' + "I'm sorry you can't go East." + '\x1b[0m')
    elif cmd == "w" or cmd == "W" or cmd == "West" or cmd == "west":
        if player.current_room.w_to:
            dir = "Go West!"
            player.current_room = player.current_room.w_to
        else:
            return print('\x1b[0;33;40m' + "I'm sorry you can't go West." + '\x1b[0m')
    else:
        return print('\x1b[0;33;40m' + "I did not understand that command" + '\x1b[0m')
    return print('\x1b[0;33;40m' + dir + '\x1b[0m' + "\n")


while True:
        print(art[player.current_room.name])
        print('\x1b[1;34;40m' + f"{player.current_room.name}" + '\x1b[0m')
        print('\x1b[1;34;40m' + f"{player.current_room.description}" + '\x1b[0m' + "\n")
        print(
            '\x1b[1;31;40m' +
            "Exits are:",
            'North' if player.current_room.n_to else '',
            'South' if player.current_room.s_to else '',
            'East' if player.current_room.e_to else '',
            'West' if player.current_room.w_to else '' + '\x1b[0m')
        print('\x1b[0;36;40m' + "****************************************************" + '\x1b[0m')
        cmd = input('\x1b[1;33;40m' + "Please input command: " + '\x1b[0m')
        if cmd == "q":
            break
        else:
            direction(player, cmd)

print("Thank you for playing")
