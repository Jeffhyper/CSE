#Defining a class
class CheeseBurger(object):
    def __init__(self, patty_type, cheese):  # TWO underscores before and two after
        self.patty = patty_type
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("You cut the cheeseburger")

    def eat(self):
        print("You eat the cheeseburger")
        self.eaten = True


#Instantiating (The creation of) two cheeseburgers
burger1 = CheeseBurger("beef", "Havarti")
burger2 = CheeseBurger ("Bacon", "Swiss")

print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)

class Car(object):
    def __init__(self, name, color ,num_of_doors, hp):
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passenger = 0
        self.name = name
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print("Nothing happens.")
        else:
            self.running = True
            print("The car starts.")

    def move_forward(self):
        if self.running:
            print("You move forward")
        else:
            print("You turn the car off")

    def go_for_drive(self,passengers):
        print("%d passenger get in." % passengers)
        self.passenger = passengers
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out." & passengers)
        self.passengers = 0


my_car = Car("Bugatti", "Blue", 4, 7458)
my_car.go_for_drive(6)