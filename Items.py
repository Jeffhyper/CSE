class Item(object):
    def __init__(self, drop, attack, defend, equip, description):
        self.drop = drop
        self.attack = attack
        self.defend = defend
        self.equip = equip
        self.description = description

    def picked_up(self):
        print("The item has been picked up.")


class Key(Item):
    def __init__(self, drop, attack, defend, equip, description, doors):
        super(Item, self).__init__(drop, attack, defend, equip, description)
        self.open = doors

    def attack(self):
        print("It did nothing.")

    def defend(self):
        print("It did nothing.")


class Jade(Key):
    def __init__(self, drop, attack, defend, equip, description, doors):
        super(Key, self).__init__(drop, equip, description, doors)

    def open_jade_door(self):
        print("The jade door is open.")

class Gold(Key):
    def __init__(self, drop, attack, defend, equip, description, doors):
        super(Key, self).__init__(drop, equip, description, doors)

    def open_chest(self):
        print("The chest is open.")

    def open_doors(self):
        print("The door is already open")


class Potion(Item):
    def __init__(self, drop, equip, description, drink):
        super(Item, self).__init__(drop, equip, description)
        self.drink = drink

    def throw(self):
        print("It did nothing.")


class Health(Potion):
    def __init__(self, drop, equip ,description):
        super(Potion, self).__init__(drop, equip, description)

    def drink(self):
        print("It restored your health.")


class Poison(Potion):
    def __init__(self, drop, equip, description):
        super(Potion, self).__init__(drop, equip, description)

    def Drink(self):
        print("You can not drink a poison potion.")

    def touched(self):
        print("You need gloves in order to get this potion.")


class Axe(Item):
    def __init__(self, drop, attack, defend, equip, description, chop):
        super(Item, self).__init__(drop, attack, defend, equip, description)
        self.chop = chop

    def chop_doors(self):
        print("The door has been chop down into wood.")


class Hamburger(Item):
    def __init__(self, drop, equip, description, eat):
        super(Item, self).__init__(drop, equip, description)
        self.eat = eat

    def eat(self):
        print("You ate the hamburger. It restored half of your health.")


class Water_Bottle(Item):
    def __init__(self, drop, equip, description, drink):
        super(Item, self).__init__(drop, equip, description)
        self.drink = drink

    def pour_water(self):
        print("You poured the water.")


class Green_Book(Item):
    def __init__(self, drop, equip, description, book):
        super(Item, self).__init__(drop, equip, description)
        self.open = book

    def read(self):
        print("You readed the book. It tells were the golden key could be.")


class lantern(Item):
    def __init__(self, drop, equip, description, glow):
        super(Item, self).__init__(drop, equip, description)
        self.glow = glow

    def turn_on(self):
        print("The lantern turns on.")


class Gloves(Item):
    def __init__(self, drop, equip, description, grab):
        super(Item, self).__init__(drop, equip, description)
        self.grab = grab

    def protect_hands(self):
        print("Your hands are now protected from things that can harm your hands.")


class Note(Item):
    def __init__(self, drop, description, clue):
        super(Item, self).__init__(drop, description)
        self.note = clue

    def read_note(self):
        print("Only one room has the key.") or print("A book that always fall off the shelf.")


class Chest(Item):
    def __init__(self, drop, description, note):
        super(Item, self).__init__(drop, description)
        self.note = note

    def use_key(self):
        print("The chest opens.")

    def opens(self):
        print("There is a letter and a gold bar.")


class letter(Item):
    def __init__(self, drop, description, read):
        super(Item, self).__init__(drop, description)
        self.read = read

    def read_note(self):
        print("Congratulations on finding the chest.")


class Gold_bar(Item):
    def __init__(self, drop, description):
        super(Item, self).__init__(drop, description)

    def use(self):
        print("It does nothing.")