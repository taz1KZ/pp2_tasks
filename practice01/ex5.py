x = "easy"
def myfunc():
  global x
  x = "hard"

myfunc()

print("Linear algebra is " + x)