"""
# Lists
the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', "beef", "sauce", "sesame seed bun", "avocado", "onions"]
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))
print(len(the_count))

# Going through lists
for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

for num in the_count:
    print(num * 2)

length = len(cheeseburger_ingredients)
range(5)  # A list of numbers 0 through 4
range(len(cheeseburger_ingredients))  # Generate a list of all indices

for num in range (len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("The item at index %d is %s" % (num,item))

# Recasting into a list
strOne = "Hello World!"
listOne = list (strOne)
print(listOne)
listOne[11] = '.'
print(listOne)

# Adding things to a list
cheeseburger_ingredients.append("Fries")
cheeseburger_ingredients.append("bread")
print(cheeseburger_ingredients)

# Remove things from a list
cheeseburger_ingredients.pop(1)
print(cheeseburger_ingredients)
cheeseburger_ingredients.remove("cheese")
print(cheeseburger_ingredients)

# Getting the alphabet
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

# Making things Lowercase
strTwo = "ThIs Is VeRY oDd sEnTenNCe"
lowercase = strTwo.lower()
print(lowercase)
l1 = ['h','e','l','l','o']

"".join(l1)
"""


# Dictionaries - Made up of keys : value pair

dictionary = {"name": 'Lance', 'age': 26, 'height': 6 * 12 + 2}

# Accessing things from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Add a pair to a dictionary
dictionary["profession"] = "telemarketer"

large_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print (large_dictionary['NY'])

larger_dictionary = {
    'CA': [
        "Fresno",
        "San Francisco"''
        'San Jose'
    ],
    'AZ': [
        "Phoenix",
        "Tuscon"
    ],
    'NY': [
        "New York City",
        "Brooklyn"
    ]
}
print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])

print(larger_dictionary['AZ'])
print(larger_dictionary['AZ'][0])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
           'Oregon',
           'Nevada',
           'Arizona'
        ]
    },

    'AZ': {
        'NAME': "Arizona",
         'POPULATION': 6931000,
         'BORDER ST': [
          'Utah',
          'Nevada',
          'New Mexico'
      ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
           'Vermont',
           'Massachuetta',
           'Connectiout',
           'Pennsylvania',
           'New Jersey'
        ]
    }
}

current_node = largest_dictionary['NY']
print(current_node['NAME'])
print(current_node['POPULATION'])

