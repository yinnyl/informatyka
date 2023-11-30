from enum import Enum

class Car:
    def __init__ (self, brand, doors, is_electric, type, color):
        self.brand = brand
        self.doors = doors
        self.is_electric = is_electric
        self.type = type
        self.color = color

    def print_car(self):
        print(f"brand: {self.brand}, doors: {self.doors}, electric: {self.is_electric}, type: {self.type}, color: {self.color}")

class Brand(Enum):
    Ferrari = 1
    Mercedes = 2

class Type(Enum):
    sportcar = 1
    van = 2

car01 = Car("Ferrari", 3, False, "sport car", "red")
car02 = Car("Mercedes", 5, False, "van", "black")

car01.print_car()
car02.print_car()