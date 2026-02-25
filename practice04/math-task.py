import math
pi = 22/7
x = int(input())
rad = x * (pi/180) # task 1 math.radians(x)
print(float(round(rad, 6)))

a = int(input())
b = int(input())
c = int(input())
print((b+c) / 2 * a) # task 2


n = int(input())
s = int(input())
area = (n * s**2) / (4 * math.tan(math.pi / n))
print(int(area))                                # task 3


g = int(input())
h = int(input())
area = g * h
print(float(round(area, 1)))        # task 4