def count_up_to(n):
  count = 1
  while count <= n:
    yield count         #instead of return, saves memory and less weights
    count += 1          # no return, but yield- no return, but saved

for num in count_up_to(5):  # the def in loop
  print(num)

gen_exp = (x * x for x in range(5))
print(gen_exp)      #weird output
print(list(gen_exp))        #listing a generator