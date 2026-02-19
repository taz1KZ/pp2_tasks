class MyNumbers:
    self.a = 1      #initialization
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration   #stopping the iterator from increasing furthert

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)