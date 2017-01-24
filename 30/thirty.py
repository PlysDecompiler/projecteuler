#https://projecteuler.net/problem=30
#531441 is 9*9**5, so no number higher than that could qualify

from itertools import product

n5 = [n**5 for n in range(10)]
numbers = set()

for i in range(2,7):
    prod = list(product('0123456789', repeat=i))
    for num in prod:
        if sum([n5[int(k)] for k in num]) == int(''.join(num)):
            nim = int(''.join(num))
            if nim not in (0,1):
                numbers.add(int(''.join(num)))
print sum(numbers), ':', len(numbers), ':', numbers

#solution: 443839
