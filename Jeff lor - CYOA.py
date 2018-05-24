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
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Key, self).__init__(name, drop, attack, defend, equip, description)

    def throw(self):
        print("It did nothing")


class Jade(Key):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Jade, self).__init__(name, drop, attack, defend, equip, description)

    def open_jade_door(self):
        Secret.east = 'Closet'


class Gold(Key):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Gold, self).__init__(name, drop, attack, defend, equip, description)

    def open_doors(self):
        Kitchen.westnorth = 'Box'
        Living.west = 'Box'


class Potion(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Potion, self).__init__(name, drop, attack, defend, equip, description)

    def drink(self):
        print("You drinked te potion")


class Health(Potion):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Potion, self).__init__(name, drop, attack, defend, equip, description)

    def drink(self):
        print("It restored your health.")


class Poison(Potion):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Potion, self).__init__(name, drop, attack, defend, equip, description)

    def drink(self):
        print("Your body starts to feel weird. You died.")


class Axe(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Axe, self).__init__(name, drop, attack, defend, equip, description)

    def swing(self):
        print("You swinged the axe.")

    def throw(self):
        print("It is too heavy to throw it.")

    def attack_with_axe(self):
        print("You attacked with the axe")


class Hamburger(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Hamburger, self).__init__(name, drop, attack, defend, equip, description)

    def eat(self):
        print("You ate the hamburger.")


class WaterBottle(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(WaterBottle, self).__init__(name, drop, attack, defend, equip, description)

    def drink(self):
        print("You drinked the water")


class GreenBook(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(GreenBook, self).__init__(name, drop, attack, defend, equip, description)

    def read(self):
        print("There was a pirate named Captain holter. He was sealed into one of the rooms by a "
              "genie and was also cursed and can never escape the room."
              "Those who enter the room, where he was sealed, didn't return.")


class Lantern(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Lantern, self).__init__(name, drop, attack, defend, equip, description)

    def turn_on(self):
        print("The lantern turns on.")

    def turn_off(self):
        print("The lantern turns off")


class Gloves(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Gloves, self).__init__(name, drop, attack, defend, equip, description)

    def use(self):
        print("You put on the gloves")

    def off(self):
        print("You took the gloves off")


class Note(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Note, self).__init__(name, drop, attack, defend, equip, description)

    def read_note(self):
        print("By using the keys, a door unlocks, you may not even know some of the doors are locked.")


class Chest(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Chest, self).__init__(name, drop, attack, defend, equip, description)

    def open(self):
        print("This chest does not have a lock hole so it cannot be opened. There seems to be some words on the chest.")

    def read(self):
        print("Thank you for playing")


class Letter(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(Letter, self).__init__(name, drop, attack, defend, equip, description)

    def read_letter(self):
        print("Welcome")


class GoldBar(Item):
    def __init__(self, name, drop, attack, defend, equip, description):
        super(GoldBar, self).__init__(name, drop, attack, defend, equip, description)

    def use(self):
        print("It does nothing.")

    def throw(self):
        print("You threw the gold bar, it came right back at your hand.")


class Character(object):
    def __init__(self, name, health, description, items=None):
        if items is None:
            items = []
        self.name = name
        self.health = health
        self.description = description
        self.inventory = items

    def pick_up_item(self, item):
        self.inventory.append(item)
        print("You picked up the item.")

    def take_damage(self, health):
        self.health -= health
        if self.health < 0:
            self.health = 0
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s" % (self.name, target.name))
        target.take_damage(20)
        target.take_damage.item.axe(30)

    def talk(self, person):
        print("%s talks %s" % (self.name, person.name))


class Pirate(Character):
    def __init__(self, name, health, description):
        super(Pirate, self).__init__(name, health, description)


class Room (object):
    def __init__(self, name, description, north, south, east, west, southeast, westnorth, item=None,
                 item_description=None, Pirate=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.westnorth = westnorth
        self.item = item
        self.item_description = item_description
        self.Pirate = Pirate

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Items
gold_bar = GoldBar("Gold bar", "The item has been dropped", "It did nothing", "This item cannot defend you",
                   "You took out the gold bar", "This item tells that there are a few more rooms to go")
chest = Chest("Chest", "The chest has been dropped", "It is too heavy.", "It's too heavy to use this as a defense",
              "You took the chest out", "The chest cannot be open.")
letter = Letter("Letter", "The letter has been dropped", "The letter is not a weapon", "It cannot defend you.",
                "You took out the letter", "The letter seems to say something.")
note = Note("Note", "The note has been dropped", "It did nothing", "It did nothing", "You took out the note.",
            "The note seems to tell what the keys do..")
gloves = Gloves("Gloves", "The gloves has been dropped", "It did nothing", "It did nothing",
                "You putted on the gloves.", "These gloves can be put on or off.")
lantern = Lantern("Lantern", "The lantern has been dropped", "You can't use a lantern to attack",
                  "A lantern cannot defend you", "The lantern has been equipped",
                  "The lantern can be turn on and turn off.")
green_book = GreenBook("Green book", "The book has been dropped", "It did nothing", "It did nothing",
                       "You took out the book", "The book seems to tell the story of the pirate")
water_bottle = WaterBottle("Water bottle", "The Item has been dropped", "It did nothing", "It did nothing",
                           "You took out the bottle", "This water bottle can restore a little of your health.")
hamburger = Hamburger("Hamburger", "The item has been dropped", "It did nothing", "It did nothing",
                      "You took out the hamburger", "When eaten, it can restore half of your health.")
axe = Axe("Axe", "The axe has been dropped", "You swing the axe", "It protected you", "You took out the axe",
          "The axe can only be use to attack.")
potion = Potion("Potion", "The potion has been dropped", "It did nothing", "It did nothing", "You took the potion out",
                "There are two types of potions, health, and poison.")
health = Health("Health potion", "The potion has been dropped", "It did nothing", "It did nothing",
                "You took the potion out", "This potion brings back full health. Use it wisely.")
poison = Poison("Poison potion", "The potion has been dropped", "It did nothing", "It did nothing",
                "You took the potion out", "You will need gloves in order to grab this potion.")
key = Key("Key", "The key has been dropped", "It did nothing", "It did nothing", "You took the key out",
          "There are two types of keys, Jade, and Gold.")
jade = Jade("jade Key", "The key has been dropped", "It did nothing", "It did nothing", "You took the jade key out",
            "This key can only open one door.")
gold = Gold("Golden Key", "The key has been dropped", "It did nothing", "It did nothing", "You took the golden key out",
            "This key can open one door.")

# Characters
character = Character("You", 100, "Your job is to explore a house and find all the items in the rooms, "
                                  "you should have a total of 14 items.")

pirate = Pirate("Captain Holter", 50,
                "This pirate is trapped in a room and will battle to escape the curse if he has to.")


# Rooms
Main = Room("The main room", "You are at the main room. There are 4 rooms. There is an axe by you", "Empty", None,
            None, None, None, None, axe, "There is an axe by you", "There is no pirate to attack")
Empty = Room("Empty room", "You are at an empty room.", None, "Main", None,
             "Garage", None, None, letter, "There is a letter in the middle of the room.", None)
Garage = Room("Garage", "You are at a garage.", "Kitchen", None, "Empty",
              None, None, None, jade, "There in a jade key in a toolbox", None)
Kitchen = Room("Kitchen", "You are at the kitchen. The are chefs cooking", None, "Garage", "Diner",
               None, None, None, hamburger, "There is a hamburger by the microwave", None)
Diner = Room("Diner room", "You are at the diner room.", None, None, "Resting",
             "Kitchen", None, None, water_bottle, "There is a water bottle by the table.", None)
Resting = Room("Resting room", "You are at a resting room. There are a lot of couches here. "
                               "People already filled them up.", "Quiet", None, None,
               "Diner", None, None, None, "There is nothing in this room", None)
Quiet = Room("Quiet room", "You are now in the quiet room. There are 3 rooms.", "Bed", "Resting", None, None, None,
             None, None, "There is nothing in this room", None)
Bed = Room("Bedroom", "You are in a bedroom.", "Computer", "Quiet", None, "Office", None, None, gloves,
           "There are two gloves by the bed", None)
Computer = Room("Computer room", "You are in a computer room. There are people typing.",
                None, "Bed", None, None, None, None, health, "There is a health potion by one of the computers.", None)
Office = Room("Office", "You are in a office. There are people working.", None, None, "Bed",
              "Hall_of_Portraits_of_art", None, None, note, "There is a note by the table", None)
Hall_of_Portraits_of_art = Room("Hall of Portraits of art", "You are at the hall of portraits of art. "
                                                            "There is nothing here.", "Work", None, "Office", "Living",
                                None, None, None, "There is nothing in this room", None)
Work = Room("Workroom", "You are at the workroom. There are 2 rooms.", None, "Hall_of_Portraits_of_art", "Lab",
            "Studio", None, None, None, "There is nothing in this room", None)
Lab = Room("Lab", "You are in the lab. There are scientist working.", None, None, None, "Work", None, None,
           poison, "There is a poison potion on a shelf", None)
Studio = Room("Studio", "You are in a studio. There are people recording.", None, None, "Work", None, None, None,
              gold_bar, "A gold bar seems to be shining at the corner of the room.", None)
Living = Room("Living room", "You are at the living room. There are 2 rooms.", None, "Mini_Library",
                             "Hall_of_Portraits_of_art", None, None, None, None, "There is nothing in this room")
Mini_Library = Room("Mini Library", "You are in Mini library. There are people reading books",
                    "Living", "Secret", None, None, None, None, green_book,
                    "There seems to be a green book on the the ground.", None)
Secret = Room("Secret Room", "You are in a secret room. There are 2 rooms.", "Mini_Library", "Camera", None, None, None,
                             None, lantern, "There is a lantern by the door", None)
Camera = Room("Camera room", "You are in a camera room. The camera's seems to show every room.", "Secret", None, None,
              None, None, None, None, "There is nothing in this room", None)
Closet = Room("Closet", "You are in a closet.", None, None, None, "Secret",
              None, None, gold, "There a a golden key in here", None)
Box = Room("Box room", "You are in a room of boxes. All boxes start to disappear", None, None, "Living", None,
           "Kitchen", None, chest, "The disappearance reveals a pirate which is Captain holter an a chest", pirate)

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
    elif 'use' in command:
        item_requested = command[4:]
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                if isinstance(item, Gloves):
                    item.use()
                elif isinstance(item, GoldBar):
                    item.use()
                elif isinstance(item, Jade):
                    item.open_jade_door()
                    print("A door unlocks")
                elif isinstance(item, Gold):
                    item.open_doors()
                    print("A door unlocks")
    elif 'jump' in command:
        print("You jumped")
    elif 'read' in command:
        item_requested = command[5:]
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                if isinstance(item, Letter):
                    item.read_letter()
                elif isinstance(item, Note):
                    item.read_note()
                elif isinstance(item, GreenBook):
                    item.read()
                elif isinstance(item, Chest):
                    item.read()
    elif 'open' in command:
        item_requested = command[5:]
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                if isinstance(item, Chest):
                    item.open()
    elif 'off' in command:
        item_requested = command[4:]
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                if isinstance(item, Gloves):
                    item.off()
                elif isinstance(item, Lantern):
                    item.turn_off()
    elif 'drink' in command:
        item_requested = command[6:]
        found = False
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                found = True
                if isinstance(item, WaterBottle):
                    item.drink()
                    character.health += 9
                elif isinstance(item, Health):
                    item.drink()
                    character.health += 30
                elif isinstance(item, Poison):
                    item.drink()
                    quit(0)
        if not found:
            print("You don't have that.")
    elif 'eat' in command:
        item_requested = command[4:]
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                if isinstance(item, Hamburger):
                    item.eat()
                    character.health += 5
    elif 'swing' in command:
        item_requested = command[6:]
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                if isinstance(item, Axe):
                    item.swing()
    elif 'turn on' in command:
        item_requested = command[8:]
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                if isinstance(item, Lantern):
                    item.turn_on()
    elif 'throw' in command:
        item_requested = command[6:]
        for item in character.inventory:
            if item.name.lower() == item_requested.lower():
                if isinstance(item, Axe):
                    item.throw()
                elif isinstance(item, GoldBar):
                    item.throw()
    elif 'look' in command:
        print(current_node.item_description)
    elif 'self' in command:
        print(character.name)
        print(character.health)
        print(character.description)
    elif 'attack' in command:
        if current_node.Pirate.health > 0:
            character.attack(current_node.Pirate)
            if current_node.Pirate.health > 0:
                if pirate.health <= 0:
                    print("The pirate died")
                current_node.Pirate.attack(character)
            if character.health <= 0:
                print("You died.")
                quit(0)
        else:
            print("There is no pirate to fight.")
    elif 'list' in command:
        for item in character.inventory:
            print(item.name)
    elif 'view' in command:
        item_requested = command[5:]
        for item in character.inventory:
            print(item.description)
    elif 'pirate data' in command:
        print(pirate.name)
        print(pirate.health)
        print(pirate.description)
    else:
        print("Command not recognized")