class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle): #1st type
  pass # still move

class Boat(Vehicle): #2nd type
  def move(self):
    print("Sail!")

class Plane(Vehicle): #3rd type
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create object
boat1 = Boat("Ibiza", "Touring 20") #Create object
plane1 = Plane("Boeing", "747")     #Create object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()