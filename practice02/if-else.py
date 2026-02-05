username = str(input())

if len(username) > 4: #check length
  print(f"Welcome, {username}!") #if meets
else: #if does not
  print("Error: Username cannot be less than", 4)