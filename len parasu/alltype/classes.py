# # # classes 

# class Vehicle:
#     def moves(self):
#         print("Moves along..")


# my_car = Vehicle()

# my_car.moves()

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#     def moves(self):
#         print("Moves along..")


# my_car = Vehicle("Tesla","Model Y")

# my_car.moves()
# print(my_car.make)
# print(my_car.model)

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#     def moves(self):
#         print("Moves along..")
#     def get_make_model(self):
#         print(f"I'm a{self.make} {self.model}.")


# my_car = Vehicle("Tesla","Model Y")

# my_car.moves()
# print(my_car.make)
# print(my_car.model)
# my_car.get_make_model()

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self):
        print("Moves along..")
    def get_make_model(self):
        print(f"I'm a{self.make} {self.model}.")


my_car = Vehicle("Tesla","Model Y")

my_car.moves()
print(my_car.make)
print(my_car.model)
my_car.get_make_model()

your_car = Vehicle('Tata', 'Nexon')
your_car.get_make_model()
your_car.moves()

print(" \n \n")
#Inheritance
class Airplane(Vehicle):
    def moves(self):
        print("Flies along....")
class Truck(Vehicle):
    def moves(self):
        print("Rumbles along....")
class GolfCart(Vehicle):
    pass

cessna = Airplane("Cessna","GC100")
mack = Truck("Mack","Pinnacle")
golfwagon = GolfCart("Yamaha","RX100")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()