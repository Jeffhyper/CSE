import random

print(random.randint(1, 7))

correctroll = 7
Money = 15
roll = 0
wrongroll = 1,2,3,4,5,6
ifwinadd = 4

print("You have 15 Dollars")
print("Roll the dice to get a number")

while roll != correctroll:
    roll = int(input(" Roll: "))

    if roll == correctroll:
        print("You've rolled to 7,you've won 4 dollars")
    elif roll == wrongroll:
        print("Wrong roll,you've lost 1 dollar")