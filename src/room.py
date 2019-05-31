# Implement a class to hold room information. This should have name and
# description attributes.

# probabley around 20 lines of code maybe less
# How to change rooms from one to the next
# "You cant go in that direction".


class Room:
    def __init__(
                self,
                name,
                description,
                n_to=None,
                s_to=None,
                e_to=None,
                w_to=None,
                items=None
    ):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = []

    def __str__(self):
        return (f'{self.name.lower()}')

    def removeItem(self, itemObj):
        for i in self.items:
            if i.name == itemObj.name:
                self.items.remove(itemObj)
                return i
        return None

    def addItem(self, itemObj):
        for i in self.items:
            if i.name == itemObj.name:
                self.items.append(itemObj)
                return i
        return None
