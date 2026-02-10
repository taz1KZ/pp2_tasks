def function(*kids): # an asterics if you dont know the number of "kids" you will have as an input
  print("The youngest child is " + kids[2]) #Index of the child i begins w 0

function("Emil", "Tobias", "Linus")


def my_function(*args): #args accepts any value acting like a tuple
  print("Type:", type(args)) #what kind of arguments
  print("First argument:", args[0]) #which one
  print("Second argument:", args[1])
  print("All arguments:", *args) #all of them, asterics to output without brackets and so on

my_function("Emil", "Tobias", "Linus")