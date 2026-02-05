x = int(input())
for x in [0, 3]:
    print(x)
    pass # avoid getting an error
for i in range(6):
  if i == 7: break #if didnot meet, doesnot break
  print(i)
else:
  print("Finally finished!")
