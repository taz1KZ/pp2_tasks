class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26 # we can modify the values based on what we need
print(p1.age)
del p1.age # we can also delete 
print(p1.name)
