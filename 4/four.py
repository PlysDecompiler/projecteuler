#https://projecteuler.net/problem=4

greatest = 0
ig,jg = 0,0

i = 100
while i < 1000:
    j = 100
    while j <= i:
        #print i,j
        k = i*j
        s = str(k)
        if s == s[::-1]:
            if k > greatest:
                greatest = k
                ig,jg = i,j
        j+=1
    i+=1

if greatest != 0:
    print greatest, "is the product of", ig, "and", jg
else: 
    print "no result"

#906609 is the product of 913 and 993
