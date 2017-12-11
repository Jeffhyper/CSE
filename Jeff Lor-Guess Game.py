# Remember, INPUTS FROM USERS ARE ALWAYS (!!!)
# OF TYPE STRING!!!!

# 1. Generate a Number
# 2. Ask the user for an input(Number)
# 3. Does the Guess match the number?
# 4. Add "Higher" and "Lower"
# 5. Add 5 guesses

print("Guessgame")

# random Numbers
import random
print(random.randint(1,50))


while guessesTaken < 5:
      print("Take a guess")
      guess = input()
      guess = int(guess)

guessesTaken = 1

