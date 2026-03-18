#Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) # index starts with a 0


#Make a search that returns no match:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt) # if no search output = "None" making it False in boolean value
print(x)