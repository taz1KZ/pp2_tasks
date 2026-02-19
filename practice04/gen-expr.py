def echo_generator():
  while True:
    received = yield
    print("Received:", received)        # gen inside

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")       #sending a values into gen
gen.send("World")      
print(next(gen)) 
gen.close()     #closes gen
