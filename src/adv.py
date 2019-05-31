from room import Room
from player import Player
from art import art
from item import Item

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

# Declare all the items
itemDict = {
    'rock': Item("Rock", """Normal looking rock""", 'outside'),
    'bone': Item("Bone", """Looks like a bone.""", 'narrow'),
    'stick': Item("Stick", """This stick might come in handy?""", 'overlook'),
    'sword': Item("Sword", """A rusty sword. Maybe you can use it?""", 'foyer'),
    'key': Item("Key", """A rusty old key that was used to open the treasure.""", 'treasure'),
}


def addItemsToRooms(item):
    for j in item:
        room[item[j].room].items.append(item[j])

addItemsToRooms(itemDict)


def removeItemFromRoom(roomName, itemName):
    room[roomName].items.remove(item[itemName])


# Terminal colors
boldRed = '\x1b[1;31;40m'
lightRed = '\x1b[0;31;40m'
boldYellow = '\x1b[1;33;40m'
lightYellow = '\x1b[0;33;40m'
lightBlue = '\x1b[0;36;40m'
boldBlue = '\x1b[1;36;40m'
lightWhite = '\x1b[0;37;40m'
endColor = '\x1b[0m'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
inputName = input(boldYellow + "Please input player's name: ")
player = Player(inputName, room['outside'])
print(lightBlue + "\n\n****************************************************\n")
print(lightBlue + f"Welcome {player.name}" + "\n")
print(lightWhite + art[player.current_room.name])
print(boldBlue + f"\n{player.current_room.name}")
print(boldBlue + f"{player.current_room.description}" + "\n")


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


cmdsDirection = [
    "n", "s", "e", "w",
    "N", "S", "E", "W",
    "North", "South", "East", "West",
    "north", "south", "east", "west"]

cmdsAction = ["get", "take", "inspect", "drop", "remove", "i", "inventory"]


def direction(player, cmd):
    if cmd[0] in ["n", "N", "North", "north"]:
        if player.current_room.n_to:
            dir = "Go North!"
            player.current_room = player.current_room.n_to
        else:
            return print(lightYellow + "I'm sorry you can't go North.")
    elif cmd[0] in ["s", "S", "South", "south"]:
        if player.current_room.s_to:
            dir = "Go South!"
            player.current_room = player.current_room.s_to
        else:
            return print(lightYellow + "I'm sorry you can't go South.")
    elif cmd[0] in ["e", "E", "East", "east"]:
        if player.current_room.e_to:
            dir = "Go East!"
            player.current_room = player.current_room.e_to
        else:
            return print(lightYellow + "I'm sorry you can't go East.")
    elif cmd[0] in ["w", "W", "West", "west"]:
        if player.current_room.w_to:
            dir = "Go West!"
            player.current_room = player.current_room.w_to
        else:
            return print(lightYellow + "I'm sorry you can't go West.")
    else:
        return print(lightYellow + "I did not understand that command")
    return [
        print(lightYellow + dir + "\n"),
        print(lightWhite + art[player.current_room.name]),
        print(boldBlue + f"{player.current_room.name}"),
        print(boldBlue + f"{player.current_room.description}" + "\n")
        ]


while True:
        print(lightRed + "Items in room are: " + f"{player.current_room.items}")
        print(
            boldRed +
            "Exits are:",
            'North' if player.current_room.n_to else '',
            'South' if player.current_room.s_to else '',
            'East' if player.current_room.e_to else '',
            'West' if player.current_room.w_to else '')
        print(lightBlue + "****************************************************")
        cmd = ' '.join(input(boldYellow + "Please input command: ").split()).split(" ")
        if cmd[0] == "q":
            break
        elif cmd[0] in cmdsDirection:
            direction(player, cmd)
        elif cmd[0] in cmdsAction:
            if cmd[0] in ['get', 'take']:
                player.addItemToPlayer(itemDict[cmd[1]])
                player.current_room.removeItem(itemDict[cmd[1]])
            elif cmd[0] in ["drop", "remove"]:
                player.removeItemToPlayer(itemDict[cmd[1]])
            elif cmd[0] in ["i", "inventory"]:
                player.getIventory()
            else:
                print(f"I didn't get that")
        else:
            print(f'That is not a command')


print("Thank you for playing" + endColor)
