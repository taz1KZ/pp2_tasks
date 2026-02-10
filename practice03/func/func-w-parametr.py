def my_f(name = "friend"): # setting f and a default value
  print("Hello", name)

my_f("Emil") #setting arguments
my_f("Tobias")
my_f() # using the name = "friend" becuz no argument
my_f("Linus")

def mammal(friend, anime):      #setting parametr
  print("I have a friend called", friend)
  print(friend + "'s from", anime)

mammal(friend = "Orachimaru", anime = "Naruto") #defining the paramets through equal sign