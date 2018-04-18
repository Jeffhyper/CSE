class Room (object):
    def __init__(self, name, description, north, south, east, west, southeast, westnorth):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.westnorth = westnorth


    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


Main = Room("The main room", "You are at the main room. There are 4 rooms.", "Empty", None, None, None, None, None)
Empty = Room("Empty room", "You are at an empty room. There is a letter in the middle of the room.", None, "Main", None, "Garage", None, None)
Garage = Room("Garage", "You are at a garage. There seems to be a key inside a toolbox.", "Kitchen", None, "Empty", None, None, None)
Kitchen = Room("Kitchen", "You are at the kitchen. There is nothing here.", None, "Garage", "Diner", None, None, "Box")
Diner = Room("Diner room", "You are at the diner room.There is a bottle of water on the table.", None, None, "Resting", "Kitchen", None, None)
Resting = Room("Resting room", "You are at a resting room.There are a lot of couches here.", "Quiet", None, None, "Diner", None, None)
Quiet = Room("Quiet room", "You are now in the quiet room.There are 3 rooms.", "Bed", "Resting,", None, None, None, None)
Bed = Room("Bedroom", "You are in a bedroom.", "Computer", None, None, "Office", None, None)
Computer = Room("Computer room", "You are in a computer room.All computers seems to be open but not turned on", None, "Bed", None, None, None, None)
Office = Room("Office", "You are in a office.There seems to be a note in one of the tables.", None, None, "Bed", "Hall_of_Portraits_of_art", None, None)
Hall_of_Portraits_of_art = Room("Hall of Portraits of art", "You are at the hall of portraits of art.", "Work", None, "Office", "Living", None, None)
Work = Room("Workroom", "You are at the workroom. There are 2 rooms.", None, "Hall_of_Portraits_of_art", "Lab", "Studio", None, None)
Lab = Room("Lab", "You are in the lab. There is a potion on a shelf.", None, "Work", None, "Studio", None, None)
Studio = Room("Studio", "You are in a studio.", None, "Work", "Lab", None, None, None)
Living = Room("Living room", "You are at the living room. There are 2 rooms.", None, "Mini_Library", "Hall_of_portraits_of_art", "Box", None, None)
Mini_Library = Room("Mini Library", "You are in Mini library. There seems to be a book on the ground.", "Living", "Secret_Basement", None, None, None, None)
Secret_Basement = Room("Secret Basement", "You are in a secret basement. There are 2 rooms.", "Mini_Library", "Camera", "Closet", None, None, None)
Camera = Room("Camera room", "You are in a camera room. The camera's seems to show every room.", "Secret_Basement", None, None, None, None, None)
Closet = Room("Closet", "You are in a closet.",  None, None, None, "Secret_Basement", None, None)
Box = Room("Box room", "You are in a room of boxes. One of the box seems to be glowing.", None, None, "Living", None, "Kitchen", None)

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
        com = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")

    else:
        print("Command not recongnized")
