world_map = {
    'WESTHOUSE': {
        'NAME': 'West of House',
        'DESCRIPTION': 'You are west of a white house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'South of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }

   }

}



current_node = world_map['WESTHOUSE']
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

