world_map = {
   'MAINROOM': {
       'NAME': 'MAIN ROOM',
       'DESCRIPTION': "You are at the main room.There are 4 rooms.",
       'PATHS': {
           'NORTH': 'EMPTY ROOM',

    'EMPTYROOM': {
        'NAME': 'EMPTY ROOM',
        'DESCRIPTION': "You are at an empty room.There is nothing here.",
        'PATHS': {
            'WEST': 'GARAGE',
    'GARAGE': {
        'NAME': 'GARAGE',
        'DESCRIPTION': "You are at a garage.There seems to be a key inside a toolbox.",
        'PATHS': {
            'EAST': 'EMPTYROOM',
            'NORTH': 'KITCHEN',
    'KITCHEN': {
        'NAME': 'KITCHEN',
        'DESCRIPTION': "You are at the kitchen.There is nothing here.",
        'PATHS': {
            'EAST': 'DINER ROOM',
            'SOUTH': 'GARAGE',
            'WESTNORTH': 'ROOM OF BOXES',
    'DINERROOM': {
        'NAME': 'DINER ROOM',
        'DESCRIPTION': "You are at the diner room.There is a glass of water on the table.",
        'PATHS': {
            'EAST': 'RESTING ROOM',
            'WEST': 'KITCHEN',
    'RESTINGROOM': {
        'NAME': 'RESTING ROOM',
        'DESCRIPTION': "You are at a resting room.There are alot of couchs here.",
        'PATHS': {
            'NORTH': 'RESTING ROOM',
            'WEST': 'DINERROOM',
    'QUIETROOM': {
        'NAME': 'QUIET ROOM',
        'DESCRIPTION': "You are now in the quiet room.There are 3 rooms.",
        'PATHS': {
            'NORTH': 'BEDROOM',
            'SOUTH': 'RESTINGROOM',
    'BEDROOM': {
        'NAME': 'BEDROOM',
        'DESCRIPTION': 'You are in a bedroom.There is a small breaker on the table next to the bed.',
        'PATHS': {
            'WEST': 'OFFICE',
            'NORTH': 'COMPUTERROOM',
    'COMPUTERROOM': {
        'NAME': "COMPUTER ROOM",
        'DESCRIPTION': "You are in a computer room.All computers seems to be open but the screen is black.",
        'PATHS': {
            'SOUTH': 'BEDROOM',
    'OFFICE': {
        'NAME': 'OFFICE',
        'DESCRIPTION': "You are in a office.There seems to be a letter in one of the tables.",
        'PATHS': {
            'EAST': 'BEDROOM',
            'WEST': 'HALL OF PICTURES',
    'HALL OF PICTURES': {
        'NAME': 'HALL OF PICTURES',
        'DESCRIPTION': "You are at the hall of pictures.",
        'PATHS': {
            'NORTH': 'WORKROOM',
            'EAST': 'QUIETROOM',
            'WEST': 'LIVING ROOM',
    'WORKROOM': {
        'NAME': 'WORKROOM',
        'DESCRIPTION': "You are at the workroom.",
        'PATHS': {
            'SOUTH': 'HALL OF PICTURES',
            'EAST': 'LAB',
            'WEST': 'STUDIO',
    'LAB': {
        'NAME': 'LAB',
        'DESCRIPTION': "You are at the lab.",
        'PATHS': {
            'WEST':'WORK ROOM',
    'STUDIO': {
        'NAME': 'STUDIO',
        'DESCRIPTION': "You are at a studio.",
        'PATHS': {
            'EAST': 'WORKROOM',
    'LIVING ROOM': {
        'NAME': 'LIVING ROOM',
        'DESCRIPTION': "You are at the living room.",
        'PATHS': {
            'EAST': 'HALL OF PICTURES',
            'WEST': 'ROOM OF BOXES',
            'SOUTH': 'LIBRARY',
    'LIBRARY': {
        'NAME': 'LIBRARY',
        'DESCRIPTION': "You are at a library.",
        'PATHS': {
            'NORTH': 'LIVING ROOM',
            'SOUTH': 'SECRET BASEMENT',
    'SECRET BASEMENT': {
        'NAME': 'SECRET BASEMENT',
        'DESCRIPTION': "You are in a secret basement.",
        'PATHS': {
            'SOUTH': 'CAMERA ROOM',
            'EAST': 'CLOSET',
    'CAMERA ROOM': {
        'NAME': 'CAMERA ROOM',
        'DESCRIPTION': "You are in a camera room.",
        'PATHS': {
            'NORTH': 'SECRET BASEMENT',
    'CLOSET': {
        'NAME': 'CLOSET',
        'DESCRIPTION': "You are in a closet. There seems to be a door.",
        'PATHS': {
            'EAST': 'OLD RESTROOM',
            'WEST': 'SECRET BASMENT',
    'OLD RESTROOM': {
        'NAME': 'OLD RESTROOM',
        'DESCRIPTION': 'You are in an old restroom.',
        'PATHS': {
            'WEST': 'CLOSET',
    'ROOM OF BOXES': {
        'NAME': 'ROOM OF BOXES',
        'DESCRIPTION': "You are in a room of boxes.",
        'PATHS': {
            'EAST': 'LIVING ROOM',
            'SOUTHEAST': 'KITCHEN',
    }
        }
    }

        }
    }
        }
    }
        }
    }
        }
    }
        }
    }
        }
    }
        }
    }
        }
    }
        }
    }
        }
    }
        }
    }

        }
    }
        }
    }

        }
    }
        }
    }

        }
    }
        }
    }
        }
    }
      }
   }
 }
}

current_node = world_map['MAIN ROOM']
direction = {'NORTH', 'SOUTH', 'EAST', 'WEST'}

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command  in direction:
        try:
          name_of_node = current_node['PATHS'][command]
          current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")

    else:
        print("Command not recongnized")