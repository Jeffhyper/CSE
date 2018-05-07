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
        print("You've found the chest. You have completed the game. The chest will give you these two wishes, "
              "you can only choose one.  Restart Game   OR   Obtain All Items  OR  None")


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


class Character(object):
    def __init__(self, name, health, description, death, items):
        self.name = name
        self.health = health
        self.description = description
        self.death = death
        self.inventory = items  # list

    def pick_up_item(self, item):
        self.inventory.append(item)
        print("You picked up the item.")

    def take_damage(self, health):
        self.health -= health
        print("You have taken damage.")


class Room (object):
    def __init__(self, name, description, north, south, east, west, southeast, westnorth, item=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.westnorth = westnorth
        self.item = item

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

# Items
gold_bar = GoldBar("Gold bar", "The item has been dropped", "It did nothing", "This item cannot defend you",
                   "You took out the gold bar", "This item will lead you to the chest, but not always.")
chest = Chest("Chest", "The chest has been dropped", "It is too heavy.", "It's too heavy to use this as a defense",
              "You took the chest out", "The chest can only be open by a gold key.")
letter = Letter("Letter", "The letter has been dropped", "The letter is not a weapon", "It cannot defend you.",
                "You took out the letter", "The letter seems to say something.", "Read the letter")
note = Note("Note", "The note has been dropped", "It did nothing", "It did nothing", "You took out the note.",
            "The note seems to tell were the last key could be.", "There are clues on this note")
gloves = Gloves("Gloves", "The gloves has been dropped", "It did nothing", "It did nothing", "You wear the gloves.",
                "These gloves can handle such things like a poison potion."
                "If it takes to many damage, it can disappear.")
lantern = Lantern("Lantern", "The lantern has been dropped", "You can't use a lantern to attack",
                  "A lantern cannot defend you", "The lantern has been equipped",
                  "The lantern can be turn on and it can help you see in the dark.", "The glow is yellow")
green_book = GreenBook("Green book", "The book has been dropped", "It did nothing", "It did nothing",
                       "You took out the book", "The book seems to tell the back story of the golden key. "
                       "You are only able to read half of it.")
water_bottle = WaterBottle("Water bottle", "The Item has been dropped", "It did nothing", "It did nothing",
                           "You took out the bottle", "This is not any ordinary water, "
                           "if you drink it you are able to hold a potion that is not holdable.")
hamburger = Hamburger("Hamburger", "The item has been dropped", "It did nothing", "It did nothing",
                      "You took out the hamburger", "When eaten, it can restore half of your health.")
axe = Axe("Axe", "The axe has been dropped", "You swing the axe", "It protected you", "You took out the axe",
          "The axe can only be use to attack and defend. If it takes to many damage, it can disappear")
potion = Potion("Potion", "The potion has been dropped", "It did nothing", "It did nothing", "You took the potion out",
                "There are two types of potions, health, and poison.", "Certain potions are drinkable")
health = Potion("Health potion", "The potion has been dropped", "It did nothing", "It did nothing",
                "You took the potion out", "This potion brings back full health. Use it wisely.",
                "You are able to drink it.")
poison = Potion("Poison potion", "The potion has been dropped", "It did nothing", "It did nothing",
                "You took the potion out", "You will need gloves in order to grab this potion.",
                "You are not able to drink it.")
key = Key("Key", "The key has been dropped", "It did nothing", "It did nothing", "You took the key out",
          "There are two types of keys, Jade, and Gold.", "Each key opens certain door")
jade = Key("jade Key", "The key has been dropped", "It did nothing", "It did nothing", "You took the jade key out",
           "This key can only open a door with a jade lock hole", "Find a jade lock hole")
gold = Key("Golden Key", "The key has been dropped", "It did nothing", "It did nothing", "You took the golden key out",
           "This key can open a chest, not doors.", "Find a chest and use this key to open it.")

# Characters
character = Character("%s", 100, "Your job is to explore an old house and find the secret of the "
                                 "chest that was made by a pirate.", "You have died", [])

# Rooms
Main = Room("The main room", "You are at the main room. There are 4 rooms.", "Empty", None, None, None, None, None,
            None)
Empty = Room("Empty room", "You are at an empty room. There is a letter in the middle of the room.", None, "Main", None,
             "Garage", None, None, letter)
Garage = Room("Garage", "You are at a garage. There seems to be a jade key inside a toolbox.", "Kitchen", None, "Empty",
              None, None, None, jade)
Kitchen = Room("Kitchen", "You are at the kitchen. There is nothing here.", None, "Garage", "Diner", None, None, "Box",
               hamburger)
Diner = Room("Diner room", "You are at the diner room. There is a water bottle on the table.", None, None, "Resting",
             "Kitchen", None, None, water_bottle)
Resting = Room("Resting room", "You are at a resting room. There are a lot of couches here.", "Quiet", None, None,
               "Diner", None, None, None)
Quiet = Room("Quiet room", "You are now in the quiet room. There are 3 rooms.", "Bed", "Resting", None, None, None,
             None, None)
Bed = Room("Bedroom", "You are in a bedroom. There seems to be a pair of gloves next to a bed.", "Computer",
           "Quiet", None, "Office", None, None, gloves)
Computer = Room("Computer room", "You are in a computer room. All computers seems to be open but turned off and "
                                 "there's a health potion next to a computer.", None,
                "Bed", None, None, None, None, health)
Office = Room("Office", "You are in a office. There seems to be a note in one of the tables.", None, None, "Bed",
              "Hall_of_Portraits_of_art", None, None, note)
Hall_of_Portraits_of_art = Room("Hall of Portraits of art", "You are at the hall of portraits of art.", "Work", None,
                                "Office", "Living", None, None, None)
Work = Room("Workroom", "You are at the workroom. There are 2 rooms.", None, "Hall_of_Portraits_of_art", "Lab",
            "Studio", None, None, None)
Lab = Room("Lab", "You are in the lab. There is a poison potion on a shelf.", None, None, None, "Work", None, None,
           poison)
Studio = Room("Studio", "You are in a studio. A gold bar seems to be shining at the corner of the room.",
              None, None, "Work", None, None, None, gold_bar)
Living = Room("Living room", "You are at the living room. There are 2 rooms. "
                             "The room on the left has a strange green lock hole", None, "Mini_Library",
                             "Hall_of_Portraits_of_art", "Box", None, None, None)
Mini_Library = Room("Mini Library", "You are in Mini library. There seems to be a green book on the the ground.",
                    "Living", "Secret", None, None, None, None, green_book)
Secret = Room("Secret Room", "You are in a secret room. There are 2 rooms."
                             "There seems to be a lantern by the door it will help you see in the dark. "
                             "The closet is locked and needs a key.", "Mini_Library", "Camera", "Closet", None, None,
                             None, lantern)
Camera = Room("Camera room", "You are in a camera room. The camera's seems to show every room."
                             "There is also an axe in a corner", "Secret", None, None, None, None, None, axe)
Closet = Room("Closet", "You are in a closet. There is a golden key on top of the shelf.", None, None, None, "Secret",
              None, None, gold)
Box = Room("Box room", "You are in a room of boxes.", None, None, "Living", None, "Kitchen", None, chest)

current_node = Main
directions = ['north', 'south', 'east', 'west', 'southeast', 'westnorth']
short_directions = ['n', 's', 'e', 'w', 'se', 'wn']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    elif "take" in command:
        item_requested = command[5:]
        if current_node.item is not None and current_node.item.name.lower() == item_requested.lower():
            character.pick_up_item(current_node.item)
            current_node.item = None

    else:
        print("Command not recognized")