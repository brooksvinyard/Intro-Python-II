class Item:
    def __init__(self, name, description, room):
        self.name = name
        self.description = description
        self.room = room

    def __repr__(self):
        return self.name
