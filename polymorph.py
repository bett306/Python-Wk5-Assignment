class Car:
    def move(self):
        return "Driving"

class Horse:
    def move(self):
        return "Galloping"
    
class Plane:
    def move(self):
        return "Flying"

class Boat:
    def move(self):
        return "Sailing"



class Snake:
    def move(self):
        return "Slithering"

# All classes have a method called move, but they implement it differently.
movers = [Car(), Plane(), Boat(), Horse(), Snake()]

for action in movers:
    print(action.move())
