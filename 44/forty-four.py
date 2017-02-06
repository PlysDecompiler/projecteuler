#https://projecteuler.net/problem=44

def pentagonal(n): 
    return (n*(3*n-1))/2

curN = 3
pents = [1,5]
k=1
j=0

while True:
    if pents[k]+pents[j] > pents[-1]:
        pents.append(pentagonal(curN))
        curN += 1
        continue
    if pents[k]+pents[j] in pents:
        if pents[k]-pents[j] in pents:
            print j+1, k+1, pents[k]-pents[j]
            break
    if k - j == 1:
        k += 1
        j = 0
    else:
        j += 1

#solution: 5482660
