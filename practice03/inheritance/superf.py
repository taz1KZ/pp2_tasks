class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname, self.grad)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)   #person f goes to student fname, lname
    self.grad = year

x = Student("Olga", "Buzova", "2019")
x.printname()
