#https://projecteuler.net/problem=22

s = open('p022_names.txt','r').read()

namelist = list(eval(s))
namelist.sort()
score = 0

def alpha(name):
    a = 0    
    for c in name:
        a+=ord(c)-64
    return a

for i,n in enumerate(namelist, 1):
    score+=i*alpha(n)

print score
#solution 871198282
