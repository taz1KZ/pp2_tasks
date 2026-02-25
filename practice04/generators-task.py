N=int(input())
s=(i**2 for i in range(1,N+1))
for num in s:
    print(num)      #lab task 1 and task 1


def even_gen(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield str(i)
n = int(input())
gen = even_gen(n)
print(",".join(gen))        #task 2


def div3_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0 and i != 0:
            yield i

n = int(input())

gen = div3_4(n)
for num in gen:
    print(num)              #task 3


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2    #any yield is generator
a = int(input())
b = int(input())
gen = squares(a, b)
for x in gen:   #if inclusive, if not then a+1, b-1
    print(x)                                #task 4


def reverse(n):
    i = 0
    while n >= i:
        yield n - i
        i += 1
n = int(input())
gen = reverse(n)
for x in gen:
    print(x)        #task 5

