from datetime import datetime, timedelta
y = datetime.now()
r =  y - timedelta(days = 5)
print(r)                # task 1

z = y - timedelta(days = 1)
x = y + timedelta(days = 1)
print(z)
print(y)
print(x)        # task 2

nomic = y.replace(microsecond = 0)
print(nomic)        # task 3

r = r - timedelta(seconds = 469)
q = r - x 
seconds = q.total_seconds()
print(seconds)