#https://projecteuler.net/problem=41
import math
from itertools import permutations

def prime(i):
    return True if all(i%n for n in range(2,int(math.sqrt(i))+1)) else False

digits = '987654321'
found = False
while not found:
    allnums = [int(''.join(perm)) for perm in permutations(digits)]
    for num in allnums:
        if prime(num):
            found = num
            break
    if not found:
        digits = digits[1:]

print found
#solution: 7652413
