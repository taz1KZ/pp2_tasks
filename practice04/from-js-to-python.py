import json #package json imported, JSON is a syntax for storing and exchanging data.
x =  '{ "name":"John", "age":30, "city":"New York"}' #some data
y = json.loads(x) #from json to python
print(y["age"]) #