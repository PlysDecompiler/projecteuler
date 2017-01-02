#https://projecteuler.net/problem=9
import math

x = 1000
a = b = c = 0

def is_square(n):
    return (math.sqrt(n) - int(math.sqrt(n))) == 0.0

found = False
while not found:
    a+=1
    b=1
    while b<a:
        c2 = a**2+b**2 
        if is_square(c2):
            c = int(math.sqrt(c2))
            if a+b+c == 1000:        
                found = True
                break
        b+=1

    if a>500:
        break

print a,b,c
print a*b*c
#solution: 31875000
