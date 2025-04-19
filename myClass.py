# This code demonstrates encapsulation, inheritance, and polymorphism in Python.
class Superhero:
    def __init__(self, name, power, level):
        self.name = name                # Public attribute
        self._power = power             # Protected attribute
        self.__strength_level = level   # Private attribute

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self._power}")
        print(f"Strength Level: {self.__strength_level}")

    def fight_crime(self):
        print(f"{self.name} is fighting crime using {self._power}!")

# Inheritance
class Batman(Superhero):
    def __init__(self, vehicle):
        super().__init__("Batman", "High Intelligence", 85)
        self.vehicle = vehicle

    def fight_crime(self):  # I'm implementing Polymorphism
        print(f"{self.name} is fighting crime and gets justice for Gotham😎.")

    def use_gadgets(self):
        print(f"{self.name} throws a Batarang!")

    def show_vehicle(self):
        print(f"{self.name}'s vehicle is the {self.vehicle}.")

# Test objects
bat1 = Batman("Batmobile")
bat2 = Batman("Batwing")

# Demonstrating polymorphism, encapsulation and inheritance
bat1.display_info()
bat1.use_gadgets()
bat1.show_vehicle()
bat1.fight_crime()

print()  # Just for spacing😁

bat2.display_info()
bat2.fight_crime()
