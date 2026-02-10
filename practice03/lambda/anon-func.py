x = lambda a, b : a * b # the elements : what action should be done
print(x(5, 6))       

"""
better to use in func()
cuz if u don't know the number to change it with
"""
def myfunc(n):
  return lambda x : x * n

quadra = myfunc(4)
u = int(input())
print(quadra(u)) #func executes via lambda and func