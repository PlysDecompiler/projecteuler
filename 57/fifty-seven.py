#https://projecteuler.net/problem=57

v = [[3,2], [7,5]]

def theNext(li):
    w1,w2 = li
    n = [2*w2[0]+w1[0], 2*w2[1]+w1[1]]
    return n
    
while len(v)<1000:
    v.append(theNext(v[-2:]))

num = 0
for el in v:
    if len(str(el[0]))> len(str(el[1])):
        num+=1

print num



#solution: 
