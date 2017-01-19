#https://projecteuler.net/problem=25
n = 2
i,j = 1,1

while True: 
    i,j = j, i+j
    n+=1
    if len(str(j)) >= 1000:
        break
# j is the nth Fibonacci-Number
print n, j, len(str(j))

#solution: 4782
