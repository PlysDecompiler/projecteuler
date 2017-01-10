#https://projecteuler.net/problem=17
from num2words import num2words

s = 0
for i in range(1, 1001):
    n = num2words(i)
    n = n.replace(' ','').replace('-','')
    s+=len(n)

print s
#solution 21124
