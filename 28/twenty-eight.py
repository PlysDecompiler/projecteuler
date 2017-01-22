#https://projecteuler.net/problem=28
#Through construction of parabolas from the 3 given points on each direction one finds the formulas for the numbers on the diagonals:
# topright: 4x^2-4x+1, bottomleft: 4x^2-8x+5, topleft: 4x^2-6x+3, bottomright: 4x^2-10x+7

s = 0

def bottomleft(n): return 4*n**2-8*n+5;
def topright(n): return 4*n**2-4*n+1;
def bottomright(n): return 4*n**2-10*n+7;
def topleft(n): return 4*n**2-6*n+3;

for i in range(1,502):
    s+=bottomleft(i)
    s+=topright(i)
    s+=bottomright(i)
    s+=topleft(i)

print s-3

#solution: 669171001
