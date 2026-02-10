class Person:                       # 1 class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
 
class student(Person): #inheriting that 1 class
    pass
x = student("Mike", "Olsen")
x.printname()