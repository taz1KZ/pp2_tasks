adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits: #inner loop, double looping # nested loop
    print(x, y)

for x in range(2, 6):
  print(x ** x) # x in the power of x