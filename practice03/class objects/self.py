class Person:
  def __init__(myobject, name, age): #myobject == self
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

#better to use self for readibility
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand #defining each
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}") #output

car1 = Car("Toyota", "Camry", 2023) # ==
car1.display_info()