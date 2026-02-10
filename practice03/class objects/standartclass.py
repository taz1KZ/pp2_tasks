class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet() #self to define
    print(message + "! Welcome to our website.")

p1 = Person("Akashi") # instant 
p1.welcome() #execution