# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__ (self, model, year, color, for_sale):                      # Variable     # self refers to the object we are currently working with
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale                                                        
        
    def drive(self):                                                        # Function
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print("You stop the car")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car3.model)
print(car3.year)
print(car3.color)
    
print()

car1.stop()
car1.drive()
car2.drive()

print()

car3.describe()
car2.describe()