
def largest_prime_factor(n):
    lpf = 2
    while n>1:
        p = 2
        while n%p:
            p+=1
        lpf = p
        print p    #(if you want to print out all prime factors)        
        n/=p
    print "result:", lpf

largest_prime_factor(600851475143)
#6857
