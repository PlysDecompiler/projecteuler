#https://projecteuler.net/problem=19
from datetime import date

numSundays = 0

i = 1901
while i<=2000:
    j = 1
    while j <= 12:
        thedate = date(i,j,1)
        if thedate.weekday() == 6:
            numSundays+=1
        j+=1
    i+=1

print numSundays
#solution: 171
