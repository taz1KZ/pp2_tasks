def fibonacci():
  a, b = 0, 1
  while True:
    yield a     #yield to save up some memory
    a, b = b, a + b     #fibonacci 
gen = fibonacci()
for _ in range(100):    # from 0 too 1
  print(next(gen))