#https://projecteuler.net/problem=48

theSum = 0

for i in range(1,1001):
    theSum += i**i
    
print str(theSum)[-10:]

#solution: 9110846700
