class Person:
  def __init__(self, name, age): #assign values with __init__ and while creating
    self.name = name #self == current instance of the class
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#if without __init__

class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25
print(p1.name)
print(p1.age)