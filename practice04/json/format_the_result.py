import json
#The json.dumps() method has parameters to make it easier to read the result:
#Use the indent parameter to define the numbers of indents:
#json.dumps(x, indent=4)
x = {
  "name": "KBTU",
  "city": "Almaty",
  "courses": ["Python", "JS", "C++"]
}


#Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))