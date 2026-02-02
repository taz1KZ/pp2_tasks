thislist = ["apple", "banana", "cherry"] # Initialization
i = 0 # for while to work
b = True # boolen value to check
while i < len(thislist): #loop to output all in [thislist]
  print(thislist[i])
  i += 1
if "apple" in thislist: #do we have apple in thislist?
  b = False # if yes, change value of b
print(b)