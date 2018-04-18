import random
"""
This is a guide of how to
 make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Take in a letter and add it to a list of letters_guessed
4. Reveal Letters based on input
5. Create the win condition
"""

words = ['dawnbreaker', 'idea', 'shiny', 'quick', 'fade', 'wish', 'aura', 'zoom', 'fast', 'brick']
randomword = random.choice(words)
print(randomword)

letters_guessed = []
guesses_left = 10
wrong_guesses = []
guesses = 0
letter = []
not_guessed = []

print(input("Guess a letter:"))
choseword = randomword


''.join(randomword)
print(randomword)

