x = "easy"
def myfunc():
  global x #changes every variable(globally)
  x = "hard" #inside a func

myfunc() # func commits

print("Linear algebra is " + x) #x has changed from easy to hard