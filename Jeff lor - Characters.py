class Character(object):
    def __init__(self, health, name, description, death, items):
        self.health = health
        self.name = name
        self.description = description
        self.death = death
        self.inventory = items  # list

    def pick_up_item(self, item):
        self.inventory.append(item)
        print("You picked up the item.")

    def take_damage(self, health):
        self.health -= health
        print("You have taken damage.")