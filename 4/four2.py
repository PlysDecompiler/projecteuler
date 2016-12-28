#https://projecteuler.net/problem=4

def is_palindrome(i):
    s = str(i)
    if s == s[::-1]:
        return True

numbers = range(10000,1000000)
numbers = [n for n in numbers if is_palindrome(n)]

for n in numbers[::-1]:
    for a in range(999,100,-1):
        if n%a == 0:
            if len(str(n/a)) == 3:
                print n, "is the product of", n/a, "and", a
                break
    else:
        continue
    break

#906609 is the product of 913 and 993
