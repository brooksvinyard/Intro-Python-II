# Write a class to hold player information, e.g. what room they are in
# currently.
blueBG = '\x1b[0;37;44m'
blueBGU = '\x1b[4;37;44m'
boldYellow = '\x1b[1;33;40m'
endColor = '\x1b[0m'


class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = []

    def getIventory(self):
        print(blueBGU + f"INVENTORY" + "\n")
        for item in self.items:
            print(blueBG + f"Name: {item.name}")
            print(blueBG + f"Description: {item.description}")
            print(blueBG + f"Found: {item.room}" + "\n")
        print(boldYellow + "\n")
        return print(boldYellow + "\n")

    def addItemToPlayer(self, inputItem):
        roomItems = self.current_room.items
        for item in roomItems:
            if item.name.lower() == inputItem.name.lower():
                self.items.append(item)
                roomItems.remove(item)
                print(boldYellow + f"\nYou have picked up {item.name}!" + "\n")
                return None
        print(boldYellow + f"\n{inputItem} is not in {self.current_room.name}" + "\n")

    def removeItemToPlayer(self, inputItem):
        roomItems = self.items
        for item in roomItems:
            if item.name.lower() == inputItem.name.lower():
                self.items.remove(item)
                print(boldYellow + f"\nYou have dropped {item.name}!" + "\n")
        return None
