class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    # Added fname and lname so we can pass them to the Parent
    def __init__(self, fname, lname, c, f):
        super().__init__(fname, lname)
        self.course = c
        self.faculty = f

    def printschool(self):
        print(f"Course: {self.course}, Faculty: {self.faculty}")
x = Student("happens", "yea", "Computer Science", "FIT - A&C")
x.printname()    # Inherited from Person
x.printschool()