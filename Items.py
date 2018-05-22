class Item(object):
    def __init__(self, name, drop, attack, defend, equip, description):
        self.name = name
        self.drop = drop
        self.attack = attack
        self.defend = defend
        self.equip = equip
        self.description = description

    def picked_up(self):
        print("The item has been picked up.")


class Key(Item):
    def __init__(self, name, drop, attack, defend, equip, description, doors):
        super(Key, self).__init__(name, drop, attack, defend, equip, description)
        self.open = doors

    def throw(self):
        print("It did nothing")


class Jade(Key):
    def __init__(self, name, drop, attack, defend, equip, description, doors):
        super(Jade, self).__init__(name, drop, attack, defend, equip, description, doors)

    def open_jade_door(self):
        print("The jade door is open.")


class Gold(Key):
    def __init__(self, name, drop, attack, defend, equip, description, doors):
        super(Gold, self).__init__(name, drop, attack, defend, equip, description, doors)

    def open_chest(self):
        print("The chest is open.")

    def open_doors(self):
        print("The door is already open")


class Potion(Item):
    def __init__(self, name, drop, attack, defend, equip, description, drink):
        super(Potion, self).__init__(name, drop, attack, defend, equip, description)
        self.drink = drink

    def throw(self):
        print("It did nothing.")


class Health(Potion):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Potion, self).__init__(name, drop, attack, defend, equip, description)

    def drink(self):
        print("It restored your health.")


class Poison(Potion):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Potion, self).__init__(name, drop, attack, defend, equip, description)

    def drink(self):
        print("You can not drink a poison potion.")

    def touched(self):
        print("You need gloves in order to get this potion.")


class Axe(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Axe, self).__init__(name, drop, attack, defend, equip, description)

    def chop_doors(self):
        print("The door has been chop down into wood.")


class Hamburger(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Hamburger, self).__init__(name, drop, attack, defend, equip, description)

    def eat(self):
        print("You ate the hamburger. It restored half of your health.")


class WaterBottle(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(WaterBottle, self).__init__(name, drop, attack, defend, equip, description)

    def pour_water(self):
        print("You poured the water.")

    def drink(self):
        print("You drinked the water")


class GreenBook(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(GreenBook, self).__init__(name, drop, attack, defend, equip, description)

    def read(self):
        print("The key was made by an old pirate many years ago. The purpose of the key is to open a chest. "
              "Inside of the chest is a mystery.")


class Lantern(Item):
    def __init__(self, name, drop, attack, defend, equip, description, glow):
        super(Lantern, self).__init__(name, drop, attack, defend, equip, description)
        self.glow = glow

    def turn_on(self):
        print("The lantern turns on.")


class Gloves(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Gloves, self).__init__(name, drop, attack, defend, equip, description)

    def protect_hands(self):
        print("Your hands are now protected from things that can harm your hands.")


class Note(Item):
    def __init__(self, name, drop, attack, defend, equip, description, clue):
        super(Note, self).__init__(name, drop, attack, defend, equip, description)
        self.note = clue

    def read_note(self):
        print("Only one room has the key.") or print("A book that always fall off the shelf.")


class Chest(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Chest, self).__init__(name, drop, attack, defend, equip, description)

    def use_key(self):
        print("The chest opens.")

    def opens(self):
        print("You've found the chest. The chest will give you these two wishes, "
              "you can only choose one.  Restart Game   OR   Obtain all Items  OR  None")


class Letter(Item):
    def __init__(self, name, drop, attack, defend, equip, description, read):
        super(Letter, self).__init__(name, drop, attack, defend, equip, description)
        self.read = read

    def read_letter(self):
        print("Welcome")


class GoldBar(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(GoldBar, self).__init__(name, drop, attack, defend, equip, description)

    def use(self):
        print("It does nothing.")


class Scroll(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Scroll, self).__init__(name, drop, attack, defend, equip, description)

    def read(self):
        print("Thank you for playing")