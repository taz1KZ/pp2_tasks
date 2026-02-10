def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Pitt", "lname": "Bradd"}
my_function(**person) # ** unpacking a person

def mfunction(**myvar): # type and amount
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

mfunction(name = "Tobias", age = 30, city = "Bergen")
"""
this is doc string 
where i can text more than 1 line
to clarify my code and it wont be seen by the code reader
"""